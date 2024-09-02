
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
    # Create the list of result
    res = []
    # Remove all punctuation in s
    s = s.replace(",", "").replace(".", "").replace("!", "").replace("?", "")
    # Create a list of all the words in s
    s_lst = s.split(" ")
    # Get all the words that contain exactly n consonants
    for word in s_lst:
        consonants = []
        for char in word:
            if char.lower() not in ["a", "e", "i", "o", "u"] and char.isalpha():
                consonants.append(char)
        if len(consonants) == n:
            res.append(word)
    return res

