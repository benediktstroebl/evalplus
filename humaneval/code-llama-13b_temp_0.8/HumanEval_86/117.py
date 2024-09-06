
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
    # # 1. get rid of trailing whitespace
    # while s.endswith(' '):
    #     s = s[:-1]
    # s = s.strip()
    #
    # # 2. split words into a list
    # words = s.split(' ')
    #
    # # 3. sort words (case-insensitive)
    # words.sort(key=str.lower)
    #
    # # 4. join words and return the result
    # return ' '.join(words)

    # # or one-liner
    # return ' '.join(word.lower() for word in sorted(s.split(' ')))

    # or
    return ' '.join(word.lower() for word in sorted(s.split(), key=str.lower))

