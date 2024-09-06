
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
    def is_consonant(letter):
        return ord(letter) < 90 and ord(letter) > 64
    def find_words(s, n):
        words = []
        for word in s.split():
            if n == count_consonants(word):
                words.append(word)
        return words
    def count_consonants(word):
        count = 0
        for letter in word:
            if is_consonant(letter):
                count += 1
        return count

    return find_words(s, n)
