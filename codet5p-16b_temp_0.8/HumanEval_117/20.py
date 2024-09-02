
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

    vowels = "aeiouy"
    s = s.split()
    
    def is_consonant(l):
        if l in vowels:
            return False
        return True
    
    def count_consonant(word):
        count = 0
        for l in word:
            if is_consonant(l):
                count += 1
        return count
    
    answer = []
    for w in s:
        if count_consonant(w) == n:
            answer.append(w)
    
    return answer

