def is_palindrome(text: str):
    """
    Checks if given string is a palindrome
    :param text: String to be checked
    :return: True if string is palindrome, else False
    """
    # Convert string to list to remove punctuation, whitespace, and lower case
    # List is reverted to maintain order
    text = list(reversed(str(text).lower()))
    # Remove all non-alphanumeric characters and return True if length is 1
    # Otherwise, compare first and last character of the list, recursively
    return (len(text) == 1 or
            (not text or
             all(isinstance(char, str) and char.isalnum() for char in text) and
             is_palindrome(text[1:] + [text[0]])))