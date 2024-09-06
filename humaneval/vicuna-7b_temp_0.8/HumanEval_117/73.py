
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
    # Your code here
    # One way to solve this problem is to convert the string to a set and then check 
    # if the set contains n consonants. If it does, then we have a valid word.
    # Otherwise, we can check if the string starts with a vowel and then check if the 
    # remaining characters contain n consonants.
    words = []
    for i in range(len(s)):
        if s[i] == ' ':
            if s[i:i+1] in set(string.ascii_letters):
                for j in range(i+1, len(s)):
                    if s[j] in set(string.ascii_letters):
                        words.append(s[i:j+1])
                        break
                    elif s[j] == 'a' or s[j] == 'e' or s[j] == 'i' or s[j] == 'o' or s[j] == 'u':
                        if len(words[-1]) == n and set(words[-1]) == set(string.ascii_letters[:n]) and s[i+1:] == s[j-1:]
                            words.append(words[-1])
                            break
                    else:
                        words.append(s[i:j+1])
                        break
    return words
