
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
    # Separate string into words
    words = s.split(" ")
    # Create empty list
    result = []
    # Create list of all consonants
    consonants = list("BDFGHJKLMNPQRSTVWXYZ")
    # Create boolean list
    test = []
    # Iterate through words in words
    for i in range(len(words)):
        # Iterate through each letter in word
        for x in words[i]:
            # If letter in consonants
            if x in consonants:
                # Add boolean to list
                test.append(True)
            # Else
            else:
                # Add boolean to list
                test.append(False)
        # If list contains n number of True
        if sum(test) == n:
            # Append word to result
            result.append(words[i])
        # Reset list
        test = []
    # Return result
    return result
