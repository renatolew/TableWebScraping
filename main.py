
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
    # Uncomment the line below if you want to check if the header content is equal to the displayed on target table
    #print('%d:"%s"' % (i, name))
    col.append((name, []))

# Now that the first row (header) is filled, we store data on the second to last row for the content
for j in range(1, len(tr_elements)):
    # T is the j'th row of the table
    T = tr_elements[j]

    # An if statement to make sure we are only storing the data from our table
    if len(T)!=10: break

    # Creating an increment for the index of our columns
    i = 0

    # Now iterating for each element of the row, instead of each row
    for t in T.iterchildren():
        data = t.text_content()
        # Check if row has empty content, if it has I want it to be skipped
        if i > 0:
            # If the content is only numerical, I want to store it as an int variable
            try:
                data = int(data)
            except:
                pass
        # Append the content data to the empty list of the i'th column
        col[i][1].append(data)
        # Increment i to repeat for next columns until the table is over
        i+=1

# Uncomment the line below to check if the lenght of each column is the same. The printed statement should return equal values to all indexes.
# print([len(C) for (title,C) in col])

# Creating a data frame to display the stored data with pandas.
Dict = {title:column for (title,column) in col}
data_frame = pd.DataFrame(Dict)

# Creating an object to write the content to an excel file and using it to write the dataframe.
writer = pd.ExcelWriter("pokedex.xlsx")
data_frame.to_excel(writer)

# Spent way too much trying to figure out why it wasn't working and noticed I forgot to actually save the file.
writer.save()
print("Dataframe written in Excel file with success.")