
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
    if s == '':
        return ''
    s = s.strip()
    new_s = []
    for i in range(len(s)):
        if i == 0 and s[i] == ' ':
            new_s.append(' ')
        if s[i] != ' ':
            new_s.append(s[i])
        if s[i] == ' ' or i == len(s) - 1:
            new_s.append(' ')
    word = []
    words = []
    for i in range(len(new_s)):
        if new_s[i] == ' ':
            words.append(''.join(word))
            word = []
        else:
            word.append(new_s[i])
    words.append(''.join(word))
    new_words = []
    for word in words:
        new_words.append(sorted(word))
    new_s = []
    for word in new_words:
        new_s.append(''.join(word))
    return ''.join(new_s).strip()

