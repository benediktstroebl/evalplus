
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
    if len(s) == 0 or n <= 0:
        return []
    
    res = []
    string = s.split()
    for word in string:
        char_counter = 0
        for char in word:
            if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
                continue
            else:
                char_counter += 1
        if char_counter == n:
            res.append(word)
    
    return res
