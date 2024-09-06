
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
    # write your code here
    result = []
    for i in range(1, len(s)):
        for j in range(i):
            if not s[j:j+n-1].isalpha():
                break
            if s[j:j+n-1] == s[i:i+n-1] or s[j:j+n-1] == s[i+1:i+n-1]:
                break
        if s[j:j+n-1] == s[i:i+n-1]:
            result.append(s[j:j+n-1])
    return result
