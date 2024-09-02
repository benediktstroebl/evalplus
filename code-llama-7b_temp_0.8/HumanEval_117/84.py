
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
    if n == 0:
        return []

    # split the string into a list of words
    words = s.split()

    # init an empty list for our results
    result = []

    # iterate through the list of words
    for word in words:
        vowels = ["a", "e", "i", "o", "u"]
        # if the length of word is equal to n
        if len(word) == n:
            # and the word is composed only of consonants (vowels)
            if set(word).issubset(vowels):
                # add it to our results list
                result.append(word)

    return result
