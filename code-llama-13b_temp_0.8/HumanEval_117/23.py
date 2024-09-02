
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


    str = []
    s = s.lower()
    x = 0
    l = len(s)
    while x < l:
        if s[x] == " ":
            str.append(" ")
            x += 1
            while x < l:
                if s[x] != " ":
                    str.append(s[x])
                    break
                x += 1
        else:
            str.append(s[x])
        x += 1


    word = ""
    nb_letter = 0
    word_list = []
    for x in str:
        if x == " ":
            if nb_letter == n:
                word_list.append(word)
            word = ""
            nb_letter = 0
        else:
            if x not in ['a', 'e', 'i', 'o', 'u']:
                word += x
                nb_letter += 1
    return word_list
