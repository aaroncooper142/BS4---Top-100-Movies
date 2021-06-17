from bs4 import BeautifulSoup
import requests


'''open and read website. had to save as html for this exercise website specs changed '''
with open("The 100 Greatest Movies _ Movies _ Empire.html") as file:
    website = file.read()
soup = BeautifulSoup(website, "html.parser")

# example of HTML looking for <h3 class="jsx-4245974604">9) Star Wars</h3>
movies = soup.find_all(name="h3", class_="jsx-4245974604")
# print(movies)

'''list comprehension to reverse list of movies starting at 1 instead of 100. 
Third element -1 will reverse the list in a loop'''
movies_list = [movie.getText() for movie in movies [::-1]]
# print(movies_list)

'''write list of top 100 movies to new text file'''
with open('movie_list.txt',"w") as file:
    for movie in movies_list:
        file.write(f"{movie}\n")


