
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
    # Note: we could implement this recursively, but I think this is more
    # clear to break down the problem and solve the problem from the hint
    if len(s) == 0:
        return []
    consonants = 0
    for i in range(len(s)):
        if s[i] in 'aeiouAEIOU':
            consonants = consonants + 1
    if consonants >= n:
        return [s]
    else:
        return select_words(s[1:], n) + select_words(s[1:], n-1)

assert(select_words("Mary had a little lamb", 4) == ["little"])
assert(select_words("Mary had a little lamb", 3) == ["Mary", "lamb"])
assert(select_words("simple white space", 2) == [])
assert(select_words("Hello world", 4) == ["world"])
assert(select_words("Uncle sam", 3) == ["Uncle"])
assert(select_words("aaaaaaaaaaaaa", 1) == [])

