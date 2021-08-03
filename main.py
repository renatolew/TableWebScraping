# To do list:
# Create Pandas DataFrame
# Export Data to a .csv or .xlsx file

import requests
import lxml.html as lh
import pandas as pd

# First step is to inspect the HTML content of the page and understand exactly where the content I want to scrap is located.
# This step makes sure I know how to use the lxml.html library to extract the exact content from the target table.
# In this project, the content is located in the table with the "pokedex" id, and all the content is in between the tr HTML tags of that table.
# It is important to note that this is the only table in this page, which makes it easier to scrap with the HTML tag as path, but in case there were more tables, I would need to specify more the path.


# Storing the URL from the page I am gonna scrap in a variable
url="https://pokemondb.net/pokedex/all"

# Creating a variable to handle the contents of the website that contains the table to be scraped
page = requests.get(url)

# Creating a variable to store the contents of the website
doc = lh.fromstring(page.content)

# Parse the table items in a new variable by getting the content that is stored between tr HTML tags.
tr_elements = doc.xpath("//tr")

# Uncomment the line below if you want to check if the lenght of the content stored in the tr_elements variable is correct.
# For this table, each row has to have exactly 10 columns.
# print([len(T) for T in tr_elements[:12]])

# Creating an empty list to parse the content and create headers.
col = []
i = 0

# Now, for each row of the table, I need to store each first element (the header) and an empty list.
for t in tr_elements[0]:
    i+=1
    name = t.text_content()
    print('%d:"%s"' % (i, name))
    col.append((name, []))

