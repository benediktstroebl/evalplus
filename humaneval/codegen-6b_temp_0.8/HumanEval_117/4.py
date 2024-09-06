
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
    return [word for word in s.split() if len(word) == n]

assert select_words("Mary had a little lamb", 4) == ["little"]
assert select_words("Mary had a little lamb", 3) == ["Mary", "lamb"]
assert select_words("simple white space", 2) == []
assert select_words("Hello world", 4) == ["world"]
assert select_words("Uncle sam", 3) == ["Uncle"]
assert select_words("", 4) == []
assert select_words("simple white space", 0) == []
assert select_words("Hello world", 0) == []
assert select_words("Uncle sam", 0) == []
assert select_words("Mary had a little lamb", 5) == ["Mary"]
assert select_words("", 0) == []
assert select_words("simple white space", 3) == []
assert select_words("Uncle sam", 1) == ["Uncle", "sam"]
assert select_words("Mary had a little lamb", 12) == ["Mary"]
assert select_words("a big black cat", 9) == ["big"]
assert select_words("a big black cat", 7) == ["big", "black"]
assert select_words("a big black cat", 8) == ["big", "black", "cat"]
assert select_words("a big black cat", 10) == ["big", "black", "cat"]
assert select_words("a big black cat", 13) == ["big", "black", "cat"]
assert select_words("a big black cat", 14) == ["big", "black", "cat"]
assert select_words("a big black cat", 15) == ["big", "black", "cat"]
assert select_words("a big black cat", 16) == ["big", "black", "cat"]
assert select_words("a big black cat", 17) == ["big", "black", "cat"]
assert select_words("a big black cat", 18) == ["big", "black", "cat"]
assert select_words("a big black cat", 19) == ["big", "black", "cat"]
assert select_words("a big black cat", 20) == ["big", "black", "cat"]
assert select_words("