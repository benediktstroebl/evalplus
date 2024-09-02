
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
    s = s.replace(" ", "").lower()
    letters = list(s)
    cons = "bcdfghjklmnpqrstvwxyz"
    cons_list = list(cons)
    cons_list_reversed = list(reversed(cons_list))
    list_cons = []
    for i in letters:
        if i in cons:
            list_cons.append(i)
    if len(list_cons) == 0:
        return []
    if len(list_cons) % n == 0:
        return [s[i : i + n] for i in range(0, len(s), n)]
    else:
        if len(list_cons) > n:
            list_cons.pop(0)
            return [s[i : i + n] for i in range(0, len(s), n)]
        else:
            list_cons.reverse()
            return [s[i : i + n] for i in range(0, len(s), n)]
