

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
    # TIP: You can use the following function to check if a char is a letter
    is_letter = lambda char: char.isalpha()
    # TIP: You can use the following function to check if a char is a number
    is_digit = lambda char: char.isdigit()

    # Check that string is not empty
    if not text:
        return True

    # Make sure the string is alphanumeric
    if not all(is_letter(char) or is_digit(char) for char in text):
        return False

    # Create a list with all the characters of the string
    chars = [char for char in text]

    # Remove all the non-letters
    chars = [char for char in chars if is_letter(char) or is_digit(char)]

    # Get the reversed list of characters
    reversed_chars = chars[::-1]

    # Compare lists
    return chars == reversed_chars
