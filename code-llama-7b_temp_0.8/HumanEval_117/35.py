
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
    # My solution 1
    # Convert string to list 
    s = s.split()
    # Use nested for loop to check for word that has n consonants 
    new_string = []
    for word in s:
        new_word = ''
        for letter in word:
            if letter.isalpha() and letter != 'a' and letter != 'e' and letter != 'i' and letter != 'o' and letter != 'u':
                new_word += letter
        if len(new_word) == n:
            new_string.append(new_word)
    return new_string
