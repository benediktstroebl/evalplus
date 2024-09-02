
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
    # The first loop will handle the "if s is empty" case
    if len(s) == 0:
        return []
    # The next loop will handle the "if n = 0" case
    if n == 0:
        return [s]
    # The next loop will handle the "if s contains n consonants" case
    words = s.split() # assuming the input string contains only letters and spaces
    consonants = 'bcdfghjklmnpqrstvwxyz' # consonants
    for word in words:
        if all(c in consonants for c in word):
            # If all the characters in the word are in the list of consonants
            # add the word to the list and continue the loop
            if len(word) < n:
                # If the word is shorter than n
                # continue the loop
                continue
            else:
                # If the word is longer than n
                # add the first n characters of the word to the list and continue the loop
                yield word[:n]
    # If all the words have been processed
    # yield the remaining word
    yield s[-n:]
