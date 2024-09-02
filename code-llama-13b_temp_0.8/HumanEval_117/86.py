
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
    # Step 1: break sentence into words.
    words = s.split()
    # Step 2: create an empty list to store selected words
    selected_words = []
    # Step 3: loop through words
    for word in words:
        # Step 3a: check if the word satisfies the criteria
        if len([l for l in word if l not in "aeiou"]) == n:
            # Step 3a(i): if it does, add the word to the selected_words list
            selected_words.append(word)
    # Step 4: return the list of selected words
    return selected_words


