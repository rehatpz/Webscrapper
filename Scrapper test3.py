#Scrapper test3

#The Data-Snatching Spider" Web Scraper Project 
#Write a script that scrapes information from websites and stores it in a database or a file.
# website to use https://www.tripadvisor.ca/

from bs4 import BeautifulSoup
import requests

try:
    # Define the URL of the TripAdvisor page
    url = 'https://www.tripadvisor.ca/Restaurants-g155032-Montreal_Quebec.html'

    # Make an HTTP GET request to fetch the webpage content
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all <a> elements containing restaurant names
        restaurant_list = soup.find_all('div', class_='restaurants-list')

        # Create a list to store restaurant names
        names = []

        # Extract restaurant names and store them in the 'names' list
        for restaurant in restaurant_list:
            restaurant_name = restaurant.text.strip() if restaurant else 'N/A'
            names.append(restaurant_name)

        # Print the extracted restaurant names
        for name in names:
            print(name)

    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")

except requests.RequestException as e:
    # Handle errors related to the HTTP request
    print(f"An error occurred during the request: {e}")

except Exception as ex:
    # Handle unexpected errors during scraping
    print(f"An unexpected error occurred: {ex}")
    

    # Open a file in write mode (creates the file if it doesn't exist)
with open('restaurant_names.txt', 'w') as file:
    # Write each restaurant name to the file
    for name in names:
        file.write(name + '\n')