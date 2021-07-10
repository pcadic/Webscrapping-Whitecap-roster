import time
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt


# Function extractText: Extracts text from scraped content.
def extractText(data):
    text = data.get_attribute('innerHTML')
    soup = BeautifulSoup(text, features="lxml")
    content = soup.get_text()
    return content


# Open website with chrome driver
#PATH = "/Users/pm/Documents/ChromeDriver/chromedriver"
PATH = "C:\\TRASH\\chromedriver.exe"

# Give the browser time to load all content.
WAIT = 5

# Open website with chrome driver
URL = "https://www.whitecapsfc.com/players"
browser = webdriver.Chrome(PATH)
browser.get(URL)

# Give the browser time to load all content.
time.sleep(WAIT)

# Get back player info
nameElements = browser.find_elements_by_css_selector(".name_link")
hometownElements = browser.find_elements_by_css_selector(".hometown")
ageElements = browser.find_elements_by_css_selector(".age")
heightElements = browser.find_elements_by_css_selector(".height")
weightElements = browser.find_elements_by_css_selector(".weight")


nameList = []
hometownList = []
ageList = []
heightList = []
weightList = []

# For each content found, append into their corresponding list
for i in range(0, len(nameElements)):

    name = extractText(nameElements[i])
    nameList.append(name)

    hometown = extractText(hometownElements[i])
    hometownList.append(hometown)

    age = extractText(ageElements[i])
    ageList.append(age)

    height = extractText(heightElements[i])
    heightList.append(height)

    weight = extractText(weightElements[i])
    weightList.append(weight)

#Create a DataFrame to store the data
#df = pd.DataFrame()
df = pd.DataFrame(columns=['Name', 'Hometown', 'Age', 'Height', 'Weight'])
for p in range(0, len(nameList)):
    playerDictionary = {'Name': nameList[p],
                        'Hometown': hometownList[p],
                        'Age': ageList[p],
                        'Height': heightList[p],
                        'Weight': weightList[p]}
    df = df.append(playerDictionary, ignore_index=True)

#Aggregation of data
dfStats = df.groupby('Age')['Name'].count().reset_index().rename(columns={'Name':'Number of player'})

#Present results in a graph
x=dfStats['Age']
y=dfStats['Number of player']

plt.bar(x,y, color='green')
plt.xlabel("Age")
plt.ylabel("Number of player")
plt.title("Number of player per age")

plt.show()

print("\nPart 2 Done")















