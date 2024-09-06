
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
    # return [word for word in s.split() if len(word) == n and word.lower().isalpha() and not word.lower().endswith("a") and not word.lower().endswith("e") and not word.lower().endswith("i") and not word.lower().endswith("o") and not word.lower().endswith("u")]
    # return [word for word in s.split() if word.lower().count("a") + word.lower().count("e") + word.lower().count("i") + word.lower().count("o") + word.lower().count("u") == len(word) - 1 and len(word) == n]
    return [word for word in s.split() if len(word) == n and word[0].lower() != "a" and word[0].lower() != "e" and word[0].lower() != "i" and word[0].lower() != "o" and word[0].lower() != "u" and word.count("a") + word.count("e") + word.count("i") + word.count("o") + word.count("u") == len(word) - 1]

