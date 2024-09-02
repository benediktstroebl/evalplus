
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

    def is_vowel(char):
        vowels = 'aeiou'
        return char in vowels

    def is_consonant(char):
        return not is_vowel(char)

    def count_consonants(s):
        cons = 0
        for char in s:
            if is_consonant(char):
                cons += 1
        return cons

    def is_word(s):
        return len(s.strip()) > 0

    cons_count = count_consonants(s)
    result = []
    for word in s.split():
        if is_word(word) and cons_count == count_consonants(word):
            result.append(word)
    return result

