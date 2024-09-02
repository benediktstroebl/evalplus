
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
    # No need for n >= len(s) as we are iterating over the string s
    # and checking each character against the set of allowed consonants
    # at each iteration, so we can avoid the extra comparison
    # between n and the length of the string s
    consonants = set(string.ascii_letters) - set(string.punctuation)
    result = []
    for char in s:
        if char.lower() in consonants:
            result.append(char)
            if len(result) == n:
                yield result
                result = []
    if result:
        yield result
