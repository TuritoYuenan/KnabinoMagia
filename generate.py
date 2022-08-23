#!/bin/python
# Batch create hugo content pages, just in case
import os, time

countries = [
	'kurdistan',
	'magical-japan',
	'magical-vietnam',
	'new-israel',
	'mashriq-arabia',
	'awteros'
]

magical_girls = [
	'leyla',
	'svitlana-zakhysnyk',
	'nataliya-narodaya',
	'sofia-konstantinos',
	'minerva-nancy-tudor',
	'marie-pasteur',
	'öttorin',
	'masa-yoshiko',
	'chloe-yang',
	'indira-periyachi',
	'mai-mai',
	'luzvi-minda',
	'xiaoyan',
	'elisheba-segel',
	'tiffany-grey',
]

#for i in countries:
#	os.system(f'hugo new countries/{i}.md')
#	time.sleep(1)
#
#for i in magical_girls:
#	os.system(f'hugo new magical-girls/{i}.md')
#	time.sleep(1)

# Drop test subject
os.system('hugo new magical-girls/test.md')
os.system('hugo new countries/test.md')
