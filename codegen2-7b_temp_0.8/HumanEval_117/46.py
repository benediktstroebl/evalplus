
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
    lista = []
    if s == "":
        return []
    if s[0].isalpha() == True:
        lista.append(s[0])
        if s[1:].isalpha() == True:
            lista.append(s[1:])
    for i in range(len(lista)):
        lista[i] = lista[i].replace(" ", "")
    return [word for word in lista if len(word) == n and word[0].isalpha()]
