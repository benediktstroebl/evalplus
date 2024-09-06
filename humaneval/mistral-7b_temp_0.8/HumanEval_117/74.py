
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
    return [w for w in s.split() if w.count('a') + w.count('e') + w.count('i') + w.count('o') + w.count('u') + w.count('y') + w.count('b') + w.count('c') + w.count('d') + w.count('f') + w.count('g') + w.count('h') + w.count('j') + w.count('k') + w.count('l') + w.count('m') + w.count('n') + w.count('p') + w.count('q') + w.count('r') + w.count('s') + w.count('t') + w.count('v') + w.count('w') + w.count('x') + w.count('z') == n]
