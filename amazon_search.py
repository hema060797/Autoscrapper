# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 09:43:03 2021

@author: l
"""


from autoscraper import AutoScraper
amazon_url="https://www.amazon.in/s?k=iphones"

wanted_list=["₹58,400","New Apple iPhone 11 (128GB) - Black"]

scraper=AutoScraper()
result=scraper.build(amazon_url,wanted_list)

print(scraper.get_result_similar(amazon_url,grouped=True))
#scraper.set_rule_aliases({'rule_fjlv':'Title','rule_8469':'Price'})
#scraper.keep_rules(['rule_fjlv','rule_8469'])
#scraper.save('amazon-search')



