
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

    if n <= 0:
        return []

    words = []
    current_word = []

    def word_occurs_n_times(s, n):
        count = 0
        for char in s:
            if char.isalpha():
                count += 1
            if count == n:
                return True
        return False

    for i in range(len(s)):
        if s[i]!='':
            current_word.append(s[i])
        else:
            if word_occurs_n_times(''.join(current_word), n):
                words.append(''.join(current_word))
            current_word = []
        if i == len(s) - 1:
            if word_occurs_n_times(''.join(current_word), n):
                words.append(''.join(current_word))
    return words


