
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
    # from re import sub, match
    # return [e for e in s.split() if len(sub("[aeiou]", "", e.lower())) == n]
    # return [e for e in s.split() if sum([e.count(i) for i in "aeiou"]) == n]
    # return [e for e in s.split() if len(match(r'[aeiou]*[b-df-hj-np-tv-xz]+[aeiou]*', e.lower()).group(0)) == n]
    
    res, acc = [], []
    for w in s.split():
        if sum(i.isalpha() for i in w) == n:
            res.append(w)
        else:
            acc += [w]
    return res

