
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
    # Find the index of the last consonant in each word
    start = 0
    end = 0
    for i in range(len(s)):
        if s[i] == " ":
            start = i
        elif s[i] == "c" or s[i] == "C":
            end = i
            break
    # Initialize a list to store the words
    words = []
    # Check each word starting from the first consonant and ending at the end of the word
    for i in range(start, len(s)):
        word = s[start:i+1]
        if (end-start) == n:
            words.append(word)
        else:
            break
    return words