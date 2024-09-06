
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
    if len(s) == 0:
        return []
    list_words = []
    list_consonants = []
    count_consonant = 0
    index = 0
    while index < len(s):
        if s[index] not in "aeiouAEIOU":
            count_consonant += 1
            list_consonants.append(s[index])
        if count_consonant == n:
            if list_consonants not in list_words:
                list_words.append(list_consonants)
            count_consonant = 0
            list_consonants = []
        index += 1
    return list_words

