from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common import action_chains
from selenium.webdriver.common.keys import Keys
import time

from selenium.webdriver.common.action_chains import ActionChains
import pyautogui
from selenium.webdriver.support.ui import WebDriverWait
driver = webdriver.Chrome()
driver.implicitly_wait(10)

def SaveAs(driver, target):
    time.sleep(3)
    actionChains = ActionChains(driver)
    actionChains.context_click(target).perform()
    
    time.sleep(1)
    pyautogui.press('up')
    pyautogui.press('up')
    pyautogui.press('up')
    pyautogui.press('up')
    pyautogui.press('up')
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    

# #login (픽시브의 경우 봇검사 시스템있기 때문에 로그인이 안되는 경우가 상당 수 있다.)
# driver.get("https://www.pixiv.net/")
# elem = driver.find_element_by_class_name("signup-form__submit--login")
# elem.click()
# id = "아이디를 입력해주세요."
# pw = "비밀번호를 입력해주세요."
# driver.find_element_by_xpath("//*[@id='LoginComponent']/form/div[1]/div[1]/input").send_keys(id)
# elem =driver.find_element_by_xpath("//*[@id='LoginComponent']/form/div[1]/div[2]/input")
# elem.send_keys(pw)
# elem.send_keys(Keys.RETURN)
# time.sleep(3)

#전체화면
driver.maximize_window ()
driver.get("https://www.pixiv.net/")

# 검색창의 주소가 로그인이 되었을 때 안되었을 때가 다르다.
#로그인o
# elem =driver.find_element_by_xpath("//*[@id='root']/div[2]/div[2]/div[1]/div[1]/div/div[2]/form/div/input")
#로그인x
elem =driver.find_element_by_xpath("//*[@id='search-bar']/div/form/input")


#검색할 단어.
elem.send_keys("桐生ココ")
elem.send_keys(Keys.RETURN)
time.sleep(5)
#검색시 모두보기 버튼이 있는경우 
try:
    tag_search=driver.find_element_by_xpath("//*[@id='root']/div[2]/div[3]/div/div[5]/div/section[2]/div[3]/a/div")
    tag_search.click()

finally:


    #이미지 갯수 저장
    img_list = driver.find_elements_by_css_selector('#root > div:nth-child(2) > div.sc-1nr368f-2.gluvRx > div > div.sc-15n9ncy-0.fDEFeI > div > section:nth-child(3) > div.l7cibp-0.hVbyIZ > ul>li')
    img_list = int(len(img_list))

    # for문 돌기
    for temp_el in range(0,img_list) :
        print(temp_el)
        el_img = driver.find_element_by_xpath("//*[@id='root']/div[2]/div[3]/div/div[5]/div/section[2]/div[2]/ul/li[{}]/div/div[1]/div/a".format(temp_el+1))
        el_img.send_keys(Keys.CONTROL +"\n")
        driver.switch_to.window(driver.window_handles[1])
        time.sleep(3)


        #좋아요 검사
        bookmark = driver.find_element_by_xpath("//*[@id='root']/div[2]/div[3]/div/div[1]/main/section/div[1]/div/figcaption/div/div/ul/li[2]/a/dl/dd")
        bookmark.get_attribute('text')
        heart=bookmark.text
        if(int(heart)>50):   
        #모두보기 버튼 검사 
            try:
                open_button = driver.find_element_by_xpath("//*[@id='root']/div[2]/div[3]/div/div[1]/main/section/div[1]/div/div[4]/div/div/button")
                img_button = driver.find_element_by_xpath("//*[@id='root']/div[2]/div[3]/div/div[1]/main/section/div[1]/div/div[4]/div/div/button/div[2]")
                open_button.click()
                move_amount = driver.find_element_by_xpath("//*[@id='root']/div[2]/div[3]/div/div[1]/main/section/div[1]/div/figure/div/div[1]/div/div/div[1]")

                #이미지 갯수
                span = driver.find_element_by_xpath("//*[@id='root']/div[2]/div[3]/div/div[1]/main/section/div[1]/div/figure/div/div[1]/div/div/div[1]/div/div/span")
                img_amount =span.text[2:]
                int_amount=int(img_amount)

                #이미지는 2부터 시작
                for i in range(0,int_amount) :
                    img_amount_url = '//*[@id="root"]/div[2]/div[3]/div/div[1]/main/section/div[1]/div/figure/div/div[{}]/div[2]/a'.format(i+2)
                    temp = driver.find_element_by_xpath(img_amount_url)
                    if (i==0) :
                        SaveAs(driver, temp)
                        time.sleep(1)
                    else :
                        move_amount.click()
                        img_temp = "/html/body/div[5]/div/div/div/div[3]/div/ul/li[{}]/div/div".format(i+1)
                        xx=driver.find_element_by_xpath(img_temp)
                        # img_temp = "/html/body/div[5]/div/div/div/div[2]/div"
                        # xx=driver.find_element_by_xpath(img_temp).text
                        time.sleep(3)
                        xx.click()
                        SaveAs(driver, temp)
                        time.sleep(1)

            except:
                #이미지 1개만 다운로드
                img_amount_url = '//*[@id="root"]/div[2]/div[3]/div/div[1]/main/section/div[1]/div/figure/div/div[1]/div/a'
                temp = driver.find_element_by_xpath(img_amount_url)
                SaveAs(driver, temp)
                time.sleep(1)
        time.sleep(3)
        driver.close()
        driver.switch_to.window(driver.window_handles[0])


            












