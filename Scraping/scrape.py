from bs4 import BeautifulSoup
import requests
import csv


a = 'https://realpython.github.io/fake-jobs/'
link = requests.get(a)

soup = BeautifulSoup(link.content,'lxml')

results = soup.find( 'div',  attrs= {'id':'ResultsContainer' , 'class' : 'columns is-multiline'})
elements = results.find_all('div' , class_ = 'card-content')
for element  in elements:                    #print only python developer in the list
    job = element.find('h2' , class_ = 'title is-5')
    company = element.find('h3' , class_ = 'subtitle is-6 company')
    location = element.find('p' , class_ = 'location')
    print(job.text.spilt())
    print(company.text.spilt())
    print(location.text.spilt())