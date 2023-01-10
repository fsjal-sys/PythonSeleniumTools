from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import urllib
import pathlib

def checkElement(driver, elementXPATH):
    """
    Takes an element's XPATH and driver as arugments.
    The driver will check if the element is in the page.
    If it is, returns true. If it isn't, returns false.
    """
    try:
        driver.find_element(By.XPATH, elementXPATH)
        return True
    except NoSuchElementException:
        return False

def downloadImage(imageElement, imageFilePath):
    """
    Takes an image element as an argument
    and uses the urllib module to download that image.
    The imageFilePath argument is a string that
    determines where the image file should be downloaded to.
    """
    urllib.request.urlretrieve(imageElement.get_attribute("src"), imageFilePath)

def tryGetting(driver, elementType, element):
    """
    Takes driver, element type, and the element path as arguments.
    The driver will look for that element and when it finds it,
    it will return the element object when it becomes accessible.
    """
    getting = True
    while getting:
        try:
            if (elementType == "CLASS_NAME"):
                element = driver.find_element(By.CLASS_NAME, element)
                getting = False
            elif (elementType == "XPATH"):
                element = driver.find_element(By.XPATH, element)
                getting = False
            return element
        except NoSuchElementException:
            continue

def createDriver():
    """
    Returns a webdriver that is ready to use for automation.
    """
    driverPath = str(pathlib.Path("chromedriver").parent.resolve())+"/chromedriver"
    return webdriver.Chrome(service=Service(driverPath))

