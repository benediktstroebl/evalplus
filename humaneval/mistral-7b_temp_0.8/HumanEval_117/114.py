
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

    def is_consonant(c):
        """Returns True if c is a consonant"""
        return c not in 'AEIOUaeiou'

    def split_words(s):
        """Returns a list of all words in the given string"""
        return s.split()

    def count_cons(s):
        """Returns the number of consonants in the string"""
        return sum(1 for c in s if is_consonant(c))

    def find_words(s, n):
        """Returns a list of all words in s that contain exactly n consonants"""
        return [w for w in split_words(s) if count_cons(w) == n]

    return find_words(s, n)
