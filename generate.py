#!/bin/python
'''Batch create hugo content pages, just in case'''
import os, time

countries = [
	'baltic-union',
	'kurdistan',
	'magical-japan',
	'indochina',
	'new-israel',
	'mashriq-arabia',
	'awteros',
	'nadoslavia'
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

for i in countries:
	os.system(f'hugo new countries/{i}.md')
	time.sleep(1)

for i in magical_girls:
	os.system(f'hugo new magical-girls/{i}.md')
	time.sleep(1)
