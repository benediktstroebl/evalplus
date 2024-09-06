
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

    # Hint: Keep the words in a list.
    # Hint: While keeping the words in the list, replace each word by
    # the ordered version of that word.
    # Hint: One more hint, to order a list of characters, sort() function
    # can be used.
    s = list(s)
    new_s = []
    i = 0
    while i < len(s):
        if s[i] != ' ':
            word = ''
            word += s[i]
            j = i + 1
            while j < len(s) and s[j] != ' ':
                word += s[j]
                j += 1
            new_s.append(''.join(sorted(word)))
            i = j
        else:
            new_s.append(' ')
            i += 1
    return ''.join(new_s)

