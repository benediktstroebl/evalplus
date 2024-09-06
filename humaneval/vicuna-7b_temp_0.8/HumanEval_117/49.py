
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
    # use a dictionary to keep track of consonant count
    consonant_count = {}
    for i in range(n):
        consonant_count[s[i]] = consonant_count.get(s[i], 0) + 1
    
    # get all words from the string s
    words = s.split(" ")
    
    # check the consonant count for each word
    words_filtered = []
    for word in words:
        if consonant_count[word[0]] == n:
            words_filtered.append(word)
    
    return words_filtered

s = "Mary had a little lamb"
print(select_words(s, 4))