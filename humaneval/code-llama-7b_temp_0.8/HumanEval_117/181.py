
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

    def is_consonant(ch):
        return (ch != 'a' and ch != 'e' and ch != 'i' and ch != 'o' and ch != 'u' and ch != ' ') and (ch == ch.upper())

    def select_consonants(s):
        consonants = []
        for ch in s:
            if is_consonant(ch):
                consonants.append(ch)
        return consonants

    words = s.split()
    return [x for x in words if len(select_consonants(x)) == n]

