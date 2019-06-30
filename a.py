
#----------------------------------IMPORT PACKAGES----------------------------------------------------------------------

from selenium import webdriver
import time



#--------------------------------------FIRST TEST CASE------------------------------------------------------------------

driver = webdriver.Firefox()
driver.get("https://www.atg.party")


driver.find_element_by_xpath("//*[contains(text(), 'Login')]").click()

#-------------------------USERNAME--------------------------------------------------------------------------------------

usrname=driver.find_element_by_id("email")
usrname.send_keys("hello@atg.world")

#------------------------PASSWORD---------------------------------------------------------------------------------------

passa=driver.find_element_by_id("password")
passa.send_keys("Pass@123")


#-----------------------------LOGIN CLICK-------------------------------------------------------------------------------

driver.find_element_by_xpath("//*[contains(text(), 'Sign in')]").click()
time.sleep(10)
#-----------------------------------FIRST COMPLETE----------------------------------------------------------------------


#------------------------------------SECOND TEST CASE ------------------------------------------------------------------


#--------------TRACING THE WRITE A POST BY HTML TAGS AND CLICKING ON ARTICLE--------------------------------------------

driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/ul/li[2]/a/ul/li[2]").click()
driver.find_element_by_xpath("//*[contains(text(),'Article')]").click()
time.sleep(1)

#-----------------ADDING TITLE AND DESCRIPTION--------------------------------------------------------------------------

title=driver.find_element_by_id("title").send_keys("TASK 1")
time.sleep(1)
driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[4]/section/div[1]/div/form/div[2]/div[2]/div[1]/div[1]/"
                             "div[2]/div").send_keys("Hi Completion of first and second  test case after clicking on "
                                                     "post button ")

time.sleep(1)

#-------------------------------CLICKING ON POST BUTTON-----------------------------------------------------------------


driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[4]/section/div[1]/div/form/div[2]/div[3]/div[4]")
driver.find_element_by_css_selector("button.btn:nth-child(7)").click()

time.sleep(5)

driver.quit()


#-------------------------------------COMPLETING BOTH TESTCASES---------------------------------------------------------