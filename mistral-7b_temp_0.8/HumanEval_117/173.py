
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
    # your code here
    list_words = s.split()
    new_list = []
    for word in list_words:
        count = 0
        if word.count('a') > 0 or word.count('e') > 0 or word.count('i') > 0 or word.count('o') > 0 or word.count('u') > 0:
            pass
        else:
            for char in word:
                if char in 'abcdefghijklmnopqrstuvwxyz':
                    count += 1
            if count == n:
                new_list.append(word)
    return new_list

