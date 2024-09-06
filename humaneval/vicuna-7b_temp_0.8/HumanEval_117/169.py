
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
    # The function starts by initializing the start and end positions to the starting index of the string
    start = 0
    end = 0
    # The function then initializes a list to store the result
    result = []
    # The function then scans the string from start to end, and for each character c in the string
    for i in range(start, end):
        # The function checks if the character is a consonant
        if ord(s[i]) >= ord('c'):
            # If it is, the function updates the start position to the next character in the string
            start = i + 1
        else:
            # If it is not, the function updates the end position to the previous character in the string
            end = i
    # The function then updates the result list to store all the words that meet the criteria
    result = [s[start:end] for start in range(len(s)) if all(ord(c) >= ord('c') for c in s[start:end]) == n]
    return result
