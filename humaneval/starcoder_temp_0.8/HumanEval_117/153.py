
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

    def select(s, n, ans, lst):
        if len(s) == 0:
            return ans
        elif len(s) == 1:
            return ans + [lst + [s]]
        elif n == 0:
            return ans + [lst]
        elif s[0] in "aeiou":
            return select(s[1:], n, ans, lst)
        else:
            return select(s[1:], n - 1, ans + [lst + [s[0]]], lst) + select(s[1:], n, ans, lst + [s[0]])

    return select(s, n, [], [])
