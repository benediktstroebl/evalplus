
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
    # your code here
    # a word is defined as a string with letters
    # a consonant is defined as a letter that is not a vowel
    # vowels are defined as the letters "aeiou"
    
    # 1. make a list of all words in s
    # 2. iterate through that list and check each word for n consonants
    # 3. add to a new list
    
    # 1. make a list of all words in s
    word_list = s.split()
    consonant_list = []
    # 2. iterate through that list and check each word for n consonants
    for word in word_list:
        consonant_count = 0
        for letter in word:
            if letter not in "aeiou":
                consonant_count += 1
        # 3. add to a new list
        if consonant_count == n:
            consonant_list.append(word)
    
    return consonant_list
    
