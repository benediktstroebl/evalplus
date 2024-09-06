
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
    if len(s.split()) == 0:
        return []

    lst = []

    #get rid of punctuation
    new_s = ""
    for i in s:
        if i.isalpha() or i.isspace():
            new_s += i

    s = new_s

    #split the string into a list of words
    word_lst = s.split()

    #find all words that contain n consonants
    for word in word_lst:
        consonant_count = 0
        for letter in word:
            if letter not in "aeiouAEIOU":
                consonant_count += 1
        if consonant_count == n:
            lst.append(word)

    return lst

