
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
    # Step 1: Get all words from the string s
    words = s.split()
    # Step 2: Create an empty list to store the words
    result = []
    # Step 3: Iterate through the words in the list
    for word in words:
        # Step 4: If the word contains exactly n consonants, append it to the result list
        if len(word) == n and sum(x in word for x in string.punctuation) == n:
            result.append(word)
    return result