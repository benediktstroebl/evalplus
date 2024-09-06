
def anti_shuffle(s):
    """
    Write a function that takes a string and returns an ordered version of it.
    Ordered version of string, is a string where all words (separated by space)
    are replaced by a new word where all the characters arranged in
    ascending order based on ascii value.
    Note: You should keep the order of words and blank spaces in the sentence.

    For example:
    anti_shuffle('Hi') returns 'Hi'
    anti_shuffle('hello') returns 'ehllo'
    anti_shuffle('Hello World!!!') returns 'Hello !!!Wdlor'
    """
    from collections import defaultdict
    a = sorted(list(s.strip()))
    d = defaultdict(list)
    for i in range(len(a)):
        d[a[i]].append(i)

    l = len(a)
    ans = ""
    for i in range(len(s.strip())):
        c = s[i]
        if c.isspace():
            ans += " "
            continue
        tmp = d[c]
        if len(tmp) == 1:
            ans += c
        else:
            ans += a[tmp[0]]
            del d[c][0]
            if len(d[c]) == 1:
                d.pop(c)

    return ans
