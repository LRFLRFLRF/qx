


from bs4 import BeautifulSoup
soup = BeautifulSoup(open("test.html",'r', encoding='UTF-8'))

res = soup.find_all("span", "txt")

list = []

for child in res:
    musicname = child.find_all(["b"])[0].get("title")
    #print(musicname)
    list.append(musicname)



res = soup.find_all("div", "text")
i = 0
j = 0
for child in res:
    if i == 1:
        i = 0
        continue

    i = 1
    musicauthor = child.find_all(["span"])[0].attrs
    musicauthor = musicauthor["title"]
    print(list[j]+'_'+musicauthor)
    j = j+1


print(res)



