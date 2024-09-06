
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
    if s != "":
        s = s.split(" ")
        word_list = []
        for word in s:
            if len(word) == n and word.count("a") == n:
                word_list.append(word)
        return word_list
    else:
        return []
assert len(select_words("Mary had a little lamb", 4)) == 1
assert len(select_words("Mary had a little lamb", 3)) == 2
assert len(select_words("simple white space", 2)) == 0
assert len(select_words("Hello world", 4)) == 1
assert len(select_words("Uncle sam", 3)) == 1
assert len(select_words("", 4)) == []
assert len(select_words("", 3)) == []
assert len(select_words("Hello world", 3)) == 0
assert len(select_words("simple white space", 4)) == 0
assert len(select_words("Simple white space", 4)) == 0
assert len(select_words("After the big white rabbit jumps over the little white patch", 4)) == 1
assert len(select_words("Simple white space", 4)) == 0
assert len(select_words("simple white space", 4)) == 0
assert len(select_words("simple white space", 6)) == 0
    