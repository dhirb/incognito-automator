#!/usr/bin/python
# -*- coding: utf-8 -*-

from selenium.webdriver import ChromeOptions, Chrome, FirefoxProfile, Firefox
import time
import re
import yaml
import argparse


class IncognitoAutomator:
    def __init__(self, browser_choice, card_to_search):
        # Set up config file
        try:
            with open('config.yml', 'r') as config_file:
                self.config = yaml.safe_load(config_file)

            # Sanity check on card name
            self.url = self.config[card_to_search]['url']
            self.search_term = self.config[card_to_search]['search_term']
        except KeyError:
            print('{card} does not exist in the config file'
                  .format(card=card_to_search))
            exit(1)
        except IOError:
            print('Config file is missing. Please download it from the source')
            exit(1)

        # Set up Selenium browser
        if browser_choice == 'chrome':
            chrome_options = ChromeOptions()
            chrome_options.add_argument('--incognito')
            self.browser = Chrome(chrome_options=chrome_options)

        elif browser_choice == 'firefox':
            firefox_profile = FirefoxProfile()
            firefox_profile.set_preference(
                'browser.privatebrowsing.autostart', True)
            self.browser = Firefox(firefox_profile=firefox_profile)

    def get_best_offer(self):
        # Open the credit card offer page
        self.browser.get(self.url)

        # Sleep to allow time for page to load
        time.sleep(self.config['wait'])

        # Find best offer search term in the page
        if re.search(self.search_term, str(self.browser.page_source)):
            # DO NOT close browser here
            # you want to apply for the best offer don't you?
            print('Found best offer')
            quit()
        else:
            self.browser.quit()


parser = argparse.ArgumentParser(
    description='Script to get best signup offer on credit cards')
parser.add_argument('-b', '--browser', action='store',
                    choices=['chrome', 'firefox'], default='chrome',
                    help='Which browser to use')
parser.add_argument('-c', '--card', action='store', required=True,
                    help='Credit card to search')
parser.add_argument('-n', '--attempt', action='store', type=int, default=20,
                    help='Number of attempts before giving up')
args = parser.parse_args()

for attempt in range(args.attempt):
    print('Attempt {attempt} of {limit}'
          .format(attempt=attempt + 1, limit=args.attempt))

    automator = IncognitoAutomator(args.browser, args.card)
    automator.get_best_offer()

print('Failed to find best offer after {attempt} attempts.'
      .format(attempt=args.attempt))
