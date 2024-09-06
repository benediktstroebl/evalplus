

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
    if len(text) == 0:
        return True

    # splits the string into half
    mid = len(text) // 2

    # if the last character does not match, return False
    if text[mid] != text[-mid - 1]:
        return False

    # recursively determine if the substrings are palindromes
    return is_palindrome(text[mid + 1:len(text)]) and is_palindrome(text[0:mid])

