# poloniex-change-address

A simple tool to change your deposit address or payment ID on Poloniex. Stop address reuse! Poloniex disabled this feature on their website but it can still be done via API.

**Note: you can only change your address or payment ID once per day, and only after it has been used once.**

## Instructions

### Clone the repository
	
	git clone https://github.com/PsychicCat/poloniex-new-address.git
	cd poloniex-new-address

### Copy your API Key, Secret, and the desired currency into the appropriate fields in `changeDEPOSIT.py`. Save the file.

	CURRENCY = 'XMR' // or whatever currency you wish to change
 	APIKEY = 'YOUR_API_KEY'
	SECRET = 'YOUR_API_SECRET'

### Execute the script from the command line.
	
	python changeDEPOSIT.py

A new deposit address will be returned, or an error message if you already have created one in the last day.





