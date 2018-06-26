import requests
import pandas as pd

##things to change:
#columnA-C: your existing row 1 values as column headers
#yourData.csv: your csv file
#responseData: you could call this something more appropriate for your API call, eg. articleDois (plural)
#columnD: this will be the header for your new column; you could call this something more appropriate for your API call, eg. doi
#response: you could call this something more appropriate for your API call, eg. articleDoi (singular)
#'published': this returns the publication date from the API. Find out which data element you wish to return in the API docs: https://api.elifesciences.org/documentation/
##to run checks, remove the hash before the code line to uncomment, and add hashes before lines you don't wish to run.

##import the list of article IDs you wish to check from a csv - credit to Stuart for this
colnames = ['columnA','columnB','columnC'] #what are the column names in your csv? TODO: If your first row is column headers, list all of these here. If your first row is not column headers, you can name your columns as you wish (note the output csv will then contain those header rows).
data = pd.read_csv('yourData.csv', names=colnames) #read in your csv file. TODO: change the filename here.
article_ids = data.columnA.tolist()[1:] #create list of article IDs from the column in your spreadsheet that contains them (here columnA), removing the first row which is the column title. TODO: change columnA to the colname as defined on line 14 OR if no column headers, remove [1:].
responseData = ['columnD'] #create new list to add pubdates to, with first entry as first row name to act as your column header.

#checks to run:
#print(len(article_ids)) #does the length of my list of article IDs correspond to the number I'm expecting from the csv?
#print(article_ids) #what does this list of article IDs look like? (i) Are the list objects in '' or not? They should be in '' to be treated as string values. (ii) Is it '/articles/#####','/articles/#####' or '/#####','/#####'. This matters for how you construct the API URL below.

##retrieve data about each article using a loop and calling the eLife API - thanks to Sean
for article_id in article_ids:
    URL = 'https://api.elifesciences.org' + article_id # if article IDs above are returned as '/articles/#####', otherwise change URL stem to add /articles/ in here.
    #print(URL) #do this to check what the URL structure is looking like - is it right? Note ../figures/ does not work for this API call; you may need to clean your entry data to get the article IDs in the right format first.
    response = ('doi') #TODO: change 'doi' to whichever element(s) you wish to retrieve from the API call.
    article = requests.get(URL).json() #this runs the API request and returns the data in JSON format.
    #print(article[pubDate]) #do this to check what your responses look like. If there are errors, check all your URLs are suitable for the API call you are making.
    responseData.append(article[response]) #add the result for each article ID to the pubdate list (adds to the bottom of the list, so order is maintained).

##add the API response data back into your csv file (help from https://www.quora.com/How-do-I-add-a-new-column-to-my-already-existing-CSV-file-using-Pandas)
data['columnD'] = responseData #define new column and specify that the data to enter here is your new list #TODO: change name to suit your data.
data.to_csv('yourData.csv') #print your new data structure, featuring a new column, back to your input csv file (you may wish to keep a duplicate of your original file before doing this, just in case).
print('csv ready') #prints 'csv ready' in your terminal once the script has finished, so you know when to check your csv file for new data.

##for a single article ID, here's how you find out something using the eLife API - credit to Sean:
#article_id = '#####' #just specify the article ID here
#URL = 'https://api.elifesciences.org/articles/' + article_id
#pubDate = ('published')
#article = requests.get(URL).json()
#print(article[pubDate]) #the response will be printed to your terminal
