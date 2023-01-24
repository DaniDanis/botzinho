import os
import pandas as pd
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome('/usr/bin/chromedriver')
driver.get('https://www.tibia.com/community/?subtopic=killstatistics')
driver.implicitly_wait(0.5)
driver.find_element(By.XPATH, value='//*[@id="killstatistics"]/div[5]/div/div/form/div/table/tbody/tr/td/div/table/tbody/tr/td/div/div[2]/select').click()
driver.implicitly_wait(0.5)
driver.find_element(By.XPATH, value='//*[@id="killstatistics"]/div[5]/div/div/form/div/table/tbody/tr/td/div/table/tbody/tr/td/div/div[2]/select/option[28]').click()
driver.find_element(By.XPATH, value='//*[@id="killstatistics"]/div[5]/div/div/form/div/table/tbody/tr/td/div/table/tbody/tr/td/div/div[3]/div').click()
tabela = driver.find_element(By.XPATH, value='//*[@id="KillStatisticsTable"]')
tabela_html = tabela.get_attribute('outerHTML')
df = pd.read_html(str(tabela_html))
df = df[0]
df.to_csv('tabelinha.csv', index=False)

