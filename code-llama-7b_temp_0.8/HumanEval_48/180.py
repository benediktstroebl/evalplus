

def is_palindrome(text: str):
    """
    Checks if given string is a palindrome
    >>> is_palindrome('')
    True
    >>> is_palindrome('aba')
    True
    >>> is_palindrome('aaaaa')
    True
    >>> is_palindrome('zbcd')
    False
    """
    text_without_spaces = text.replace(" ", "")
    text_without_spaces_without_punctuation = text_without_spaces.translate(str.maketrans('', '', ".,?!:;"))

    if text_without_spaces_without_punctuation == text_without_spaces_without_punctuation[::-1]:
        return True
    else:
        return False

