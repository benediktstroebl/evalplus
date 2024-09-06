

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
    result = True
    if len(text) % 2 == 1:
        text = text[:len(text)//2]
        for i in range(len(text)):
            if text[i] != text[-1-i]:
                result = False
                break
    else:
        for i in range(len(text)//2):
            if text[i] != text[-1-i]:
                result = False
                break
    return result

