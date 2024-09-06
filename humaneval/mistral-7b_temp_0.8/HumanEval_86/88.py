
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
    def anti_shuffle_words(s):
        l = []
        for word in s.split(' '):
            if not word: continue
            l.append(''.join(sorted(word)))
        return ' '.join(l)
    if not s: return s
    l = []
    for i in s:
        if i.isspace():
            l.append(i)
            continue
        l.append(''.join(sorted(list(i))))
    return ''.join(l)
