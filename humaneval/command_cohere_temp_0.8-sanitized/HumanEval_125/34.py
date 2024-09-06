import re
def split_words(txt):
    """
    Split the given string of words into a list, exploiting whitespace or comma separation.
    If the text does not contain whitespace or comma, return the count of lower-case letters
    with odd alphabetical order.
    """
    if re.match(r'[^\s,]+', txt):
        return txt.split(' ')
    elif re.match(r'[^,]+', txt):
        return txt.split(',')
    else:
        return len([char for char in txt if ord(char) % 2 == 0 and char.islower()])