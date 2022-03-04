# -*- coding:utf-8 -*-
__author__ = 'qijia'
__date__ = '2022/3/4 2:28 下午'

from selenium import webdriver  # 用来驱动浏览器的
from selenium.webdriver import ActionChains  # 破解滑动验证码的时候用的 可以拖动图片
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By  # 按照什么方式查找，By.ID,By.CSS_SELECTOR
from selenium.webdriver.common.keys import Keys  # 键盘按键操作
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC  # 和下面WebDriverWait一起用的
from selenium.webdriver.support.wait import WebDriverWait  # 等待页面加载某些元素
import time


def process_result_set(driver, url):
    driver.get(url)
    # search_windows = driver.current_window_handle
    # driver.find_element_by_id("kw").send_keys("rei")
    # driver.find_element_by_id("su").click()
    div_result = driver.find_element_by_id("search-results")
    li_results = div_result.find_element_by_tag_name("ul").find_elements_by_tag_name("li")
    # time.sleep(10)
    return li_results

# def process_product_list(product_ele:WebElement):
#     return

def run():
    # 配置
    options = Options()
    # options.add_argument("--kiosk")
    options.add_experimental_option("detach", True)
    # options.add_argument()
    # 总调度
    rei_arcteryx_url = "https://www.rei.com/search?q=arcteryx+mens&ir=q%3Aarcteryx+mens&r=deals%3ASee+All+Deals%3Bsize%3AMedium%7C34+Waist%7CLarge"
    rei_patagonia_url = "https://www.rei.com/search?q=patagonia+mens&ir=q%3Aarcteryx+mens&r=deals%3ASee+All+Deals%3Bsize%3AMedium%7C34+Waist"
    bc_arcteryx_url = ""
    bc_patagonia_url = ""
    bc_mammut_url = ""
    sc_arcteryx_url = ""
    sc_patagonia_url = ""
    sc_mammut_url = ""
    the_last_hunt_arcteryx_url = ""
    the_last_hunt_valience_url = ""
    the_altitude_sport_arcteryx_url = ""
    mj_mammut_url = ""
    ms_mammut_url = ""

    # config_dict = {
    #     "rei": {
    #         "arcteryx": rei_arcteryx_url,
    #         "patagonia": rei_patagonia_url
    #     }
    # }
    rei_config = {
        "website":"rei",
        "urls":[rei_arcteryx_url, rei_patagonia_url]
    }
    driver = webdriver.Chrome("/Users/qijia/app/pachong/chromedriver", options=options)
    for url in rei_config["urls"]:
        product_list_without_check = process_result_set(driver, url)
        product_url_list = []
        for product_ele in product_list_without_check:
            tag_a = product_ele.find_element_by_tag_name("a")
            product_url = tag_a.get_attribute("href")
            product_url_list.append(product_url)
        print("rei"+product_url_list)
    driver.quit()
    driver.close()


if __name__ == "__main__":
    run()
