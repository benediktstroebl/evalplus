
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
    result = []
    count = 0
    for i in range(len(s)):
        if (s[i] == ' ' and count == n) or (s[i] == 'c' and count == n):
            result.append(s[i] + s[i+1:])
            count = 0
        elif (s[i] == ' ' or s[i] == 'c') and count == n:
            count += 1
        elif (s[i] == 'c' and count > n) or (s[i] == ' ' and count > n):
            break
    for i in result:
        if len(i) > 0:
            result.append(i)
    return result
