
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

    s = s.split()
    # print(s)
    consonants = "bcdfghjklmnpqrstvwxyz"
    new_s = []
    for word in s:
        new_word = ""
        for letter in word:
            if letter.lower() in consonants:
                new_word += letter
        new_s.append(new_word)

    # print(new_s)
    final_s = []
    for word in new_s:
        if len(word) == n:
            final_s.append(word)

    return final_s

