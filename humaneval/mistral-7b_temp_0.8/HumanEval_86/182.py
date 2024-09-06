
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
    if not s:
        return ''
    result = ''
    for i in range(len(s)):
        word = s[i:i + len(s[i])].lower()
        if word[0].isalpha():
            result += word[0].lower() + word[1:][::-1] + ' '
    return result[:-1]
