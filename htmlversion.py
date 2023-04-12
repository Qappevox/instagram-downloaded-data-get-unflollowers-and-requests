from bs4 import BeautifulSoup


def get_followers():
    followers_list = ""
    with open("followers_1.html", "r", encoding="utf-8") as f:
        html = f.read()
        f.close()
    
    soup = BeautifulSoup(html, 'html.parser')

    for div in soup.find_all('div', {'class': 'pam _3-95 _2ph- _a6-g uiBoxWhite noborder'}):
        username = div.find('a').text
        #print(username)
        followers_list = followers_list + username + "\n"
    return followers_list

def get_following():
    following_list = ""
    with open("following.html", "r", encoding="utf-8") as f:
        html = f.read()
        f.close()
    
    soup = BeautifulSoup(html, 'html.parser')

    for div in soup.find_all('div', {'class': 'pam _3-95 _2ph- _a6-g uiBoxWhite noborder'}):
        username = div.find('a').text
        following_list = following_list + username + "\n"
        #print(username)

    return following_list

def get_requests():
    with open("follow_requests_you've_received.html", "r", encoding="utf-8") as f:
        html = f.read()
        f.close()
    
    soup = BeautifulSoup(html, 'html.parser')
    counter = 0
    for div in soup.find_all('div', {'class': 'pam _3-95 _2ph- _a6-g uiBoxWhite noborder'}):
        username = div.find('a').text
        print(username)
        counter = counter + 1
    return counter
    
def find_diff(followers, following):
    fs = followers
    fg = following
    s1 = fg
    s2 = fs
    s1 = s1.split()
    unfollowers = ""
    for i in s1:
        if i not in s2:
            unfollowers = unfollowers + i + "\n"
    #print(unfollowers)
    return unfollowers

get_following()
get_followers()


result = find_diff(followers=get_followers(), following=get_following())
print(result)
count = get_requests()

print(count)

#I didn't put too much effort into writing this code, but I wanted to include the HTML version as well.
