

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

    if not isinstance(text, str):
        raise TypeError(f'expected str, but got {type(text)}')

    text_without_spaces = text.replace(' ', '')
    text_without_spaces_without_case = text_without_spaces.lower()

    for i in range(len(text_without_spaces_without_case)):
        first_letter = text_without_spaces_without_case[i]

        last_index_of_text = len(text_without_spaces_without_case) - 1 - i

        last_letter = text_without_spaces_without_case[last_index_of_text]
        if first_letter != last_letter:
            return False

    return True

