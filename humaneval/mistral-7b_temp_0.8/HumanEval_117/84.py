
def select_words(s, n):
    """Given a string s and a natural number n, you have been tasked to implement 
    a function that returns a list of all words from string s that contain exactly 
    n consonants, in order these words appear in the string s.
    If the string s is empty then the function should return an empty list.
    Note: you may assume the input string contains only letters and spaces.
    Examples:
    select_words("Mary had a little lamb", 4) ==> ["little"]
    select_words("Mary had a little lamb", 3) ==> ["Mary", "lamb"]
    select_words("simple white space", 2) ==> []
    select_words("Hello world", 4) ==> ["world"]
    select_words("Uncle sam", 3) ==> ["Uncle"]
    """
    words = s.split()
    count = 0
    ans = []
    for i in range(len(words)):
        temp = words[i].split('')
        for j in range(len(temp)):
            if(ord(temp[j])>=65 and ord(temp[j])<=90 or ord(temp[j])>=97 and ord(temp[j])<=122):
                count+=1
            else:
                continue
        if(count == n):
            ans.append(words[i])
        count = 0
    return ans
