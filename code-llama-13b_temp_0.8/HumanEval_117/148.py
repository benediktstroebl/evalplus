
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
    # def contains(word, number):
    #     consonants = "bcdfghjklmnpqrstvwxyz"
    #     for i in consonants:
    #         count = 0
    #         for j in word:
    #             if i == j:
    #                 count += 1
    #         if count == number:
    #             return True
    #     return False

    # words = s.split()
    # selected_words = []
    # for word in words:
    #     if contains(word, n):
    #         selected_words.append(word)
    # return selected_words

    consonants = "bcdfghjklmnpqrstvwxyz"
    selected_words = []
    for word in s.split():
        count = 0
        for i in word:
            if i in consonants:
                count += 1
        if count == n:
            selected_words.append(word)
    return selected_words

