# Import
import pandas as pd
import requests
from bs4 import BeautifulSoup
import csv
# User agent of the website
header = {'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"}

# Access the data of restaurant
def items(response,code):
    csv_file = open('hyd.csv', 'w')
    writer = csv.writer(csv_file)
    writer.writerow(['Restaurant Name', 'Rating', 'Cuisine', 'Location'])

    x = []
    if response.status_code == code:
        soup = BeautifulSoup(response.text,'html.parser')     

        restaurant_element = soup.find_all('div', class_='styled__StyledRestaurantGridCard-sc-fcg6mi-0 lgOeYp')


        for restaurant in restaurant_element:
            # Extract information from each <a> element and its child <div> elements
            restaurant_name = restaurant.find('div', class_='sc-beySbM cwvucc').text.strip()
            rating = restaurant.find('span', class_='sc-beySbM evFhcR').text.strip()
            data = restaurant.find_all('div', class_='sc-beySbM iTWFZi')
       

            print(f'Restaurant Name: {restaurant_name}')
            print(f'Rating: {rating}')
            print(f'Cuisine: {data[0].text.strip()}')
            print(f'Location: {data[1].text.strip()}')
            
            # write the data to csv file
            writer.writerow([restaurant_name, rating, data[0].text.strip(), data[1].text.strip()])    

# Main code of environment
def maincode(url):
    response = requests.get(url, headers=header)
    code = response.status_code

    if response.status_code == code:
        soup = BeautifulSoup(response.text, 'html.parser')
    items(response, code)

# Execution of program
if __name__ == "__main__":
    url = f"https://www.swiggy.com/city/hyderabad"
    maincode(url)