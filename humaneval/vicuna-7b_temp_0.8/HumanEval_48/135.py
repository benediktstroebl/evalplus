

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
    return text == text[::-1]

@given(text=st.text(min_size=1, max_size=100, unique=True),
       x=st.text(min_size=1, max_size=100, unique=True))
