# Incognito Automator

A Python script to automate your (endless) quest to search for the best credit card sign up offer.

Flow of the script:

1. Opens the URL of the specified credit card.
2. Waits for the page to load completely.
3. Searches for the specified search term.

  * If found, the script ends while leaving the browser window opened.
  * If not found, closes the browser window and repeat step 1 until attempt limit is reached or best offer found.

## Getting Started

Clone this repository to your local computer.

### Prerequisites

1. Python 2.7.15 or Python 3.7.0 (older versions may work but not tested)
2. [pip](https://pip.pypa.io/en/stable/installing/)
3. Project dependencies
```
pip install -r requirements.txt
```

## Usage

``` 
python incognito_automator.py --card prg --browser firefox --attempt 5
```

### Arguments

##### `-c` or `--card`
Required. Specify which credit card to search for best offer. More cards can be added to `config.yml`.

##### `-b` or `--browser`
Optional. Specify which browser to use. Default: Google Chrome.

##### `-n` or `--attempt`
Optional. Specify number of attempts to find best offer before giving up. Default: 20.


### Supported credit cards (US only)

* American Express Platinum
* American Express Premier Rewards Gold
* American Express Green

Alternatively, you can add the URL and the search term for more credit cards in `config.yml` using the following syntax:
```yaml
card_name:
  url: URL_of_the_credit_card_page
  search_term: text_to_search_which_indicates_a_better_offer
```

### Supported browsers

* Google Chrome
* Mozilla Firefox

### Tested with

* Python 2.7.15
* Python 3.7.0

Older Python versions may work.

## Disclaimer

This script serves as a tool to assist in searching for best credit card sign up offers, it does not guarantee any successful search for offers, public or otherwise. 

## License

This project is licensed under the MIT License.

## Acknowledgments

* Stack Overflow for tips on Selenium usage
* [argparse](https://docs.python.org/3/library/argparse.html) documentation
