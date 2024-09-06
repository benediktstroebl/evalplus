
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
    if len(s) == 0:
        return s
    elif s[0] == ' ':
        return s[0] + anti_shuffle(s[1:])
    else:
        if len(s.split()) > 1:
            # Get the string upto the first space character
            # and call anti_shuffle on the rest of the string
            first_word, rest_of_the_string = s.split(' ', 1)
            return first_word + anti_shuffle(rest_of_the_string)
        else:
            # If there are no spaces in the string
            # then all the characters are part of the same word
            # Get the string upto the first space character
            # and call anti_shuffle on the rest of the string
            return ''.join(sorted(list(s)))
