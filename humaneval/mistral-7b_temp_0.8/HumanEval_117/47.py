
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

    # from string import ascii_lowercase
    # consonants = ''.join(ascii_lowercase[i] for i in range(14, 22))
    # vowels = ''.join(ascii_lowercase[i] for i in range(4, 14))
    # consonants = "bcdfghjklmnpqrstvwxyz"
    # vowels = "aeiou"
    # Consonants can be obtained as follows:
    # consonants = "bcdfghjklmnpqrstvwxyz"
    # Consonants can also be obtained as follows:
    # consonants = "".join(chr(x) for x in range(ord("b"), ord("z") + 1))
    # Vowels can be obtained as follows:
    # vowels = "aeiou"
    # Vowels can also be obtained as follows:
    # vowels = "".join(chr(x) for x in range(ord("a"), ord("e") +
