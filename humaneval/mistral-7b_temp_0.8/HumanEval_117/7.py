
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
    # Replace this line with your code.
    words = s.split()
    new_list = []
    for i in words:
        consonants = 0
        if i == words[-1]:
            consonants += 1
        for j in i:
            if ord(j) > 96 and ord(j) < 123:
                if j.isalpha() and j.isupper():
                    consonants += 1
        if consonants == n:
            new_list.append(i)
    return new_list
