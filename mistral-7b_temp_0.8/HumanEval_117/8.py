
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
    word = []
    index = 0
    for i in s:
        if i.isalpha():
            word.append(i)
        elif i == ' ':
            if len(word) == n:
                if len(word) != 0:
                    index += 1
                    if index in [i for i in range(1, n + 1)]:
                        if word not in word_list:
                            word_list.append(word)
                            word = []
                else:
                    pass
            else:
                pass
    return word_list
