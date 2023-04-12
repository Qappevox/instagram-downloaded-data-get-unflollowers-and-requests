

import json

def create_file(file_name, content):
    with open(file_name, "w") as f:
        f.write(content)
        f.close()
    return None

def count_it(text, target):
    import re
    pattern = fr'\b({target})\b'
    count = len(re.findall(pattern, text))
    #print(f'"{target}" : {count}')
    return count


def get_followers():
    followers_list = ""
    with open("followers_1.json", "r") as f:
        data = f.read()
        count = count_it(data, "value") #following count
        data = json.loads(data)
        for i in range(count):
            #print(data[i][ "string_list_data"][0]["value"])
            followers_list = followers_list + data[i][ "string_list_data"][0]["value"] + "\n"
        #print(type(data))
        f.close()
    return followers_list

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


def get_following():
    following_list = ""
    with open("following.json", "r") as f:
        data = f.read()
        count = count_it(data, "value") #following count
        data = json.loads(data)
        for i in range(count):
            #print(data["relationships_following"][i]["string_list_data"][0]["value"])
            following_list = following_list + data["relationships_following"][i]["string_list_data"][0]["value"] + "\n"
        #print(type(data))
        f.close()
    return following_list

def get_follow_requests():
    requests_list = ""
    with open("follow_requests_you've_received.json", "r") as f:
        data = f.read()
        count = count_it(data, "value")
        data = json.loads(data)
        for i in range(count):
            #print(data["relationships_follow_requests_received"][i]["string_list_data"][0]["value"])
            requests_list = requests_list + data["relationships_follow_requests_received"][i]["string_list_data"][0]["value"] + "\n"
        f.close()
        requests_list = requests_list + "\n    total:" + str(count)
    return requests_list



def main():
    following = get_following()
    followers = get_followers()
    #find_diff(followers, following)
    #get_follow_requests()
    create_file("requests.txt", get_follow_requests())
    create_file("unfollowers.txt", find_diff(followers, following))
    
main()
