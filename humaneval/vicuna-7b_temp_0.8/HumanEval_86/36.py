
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
    # check if string is empty
    if not s:
        return ''

    # check if string only contains letters
    if not any(c.isalpha() for c in s):
        return ''

    # split the string on whitespaces
    words = s.split()

    # reverse the string
    words = [word[::-1] for word in words]

    # reassemble the string with characters in ascending order
    reassemble_words = []
    for word in words:
        reassemble_words.append(chr(ord('a') - 1 + len(word)))

    # join the words back to a string
    reassembled_string = ''.join(reassemble_words)

    return reassembled_string
