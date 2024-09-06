def is_palindrome(text: str):
    """
    Checks if given string is a palindrome
    :param text: String to be checked
    :return: True if string is palindrome, False otherwise
    """
    # Convert string to list to allow indexing from both sides
    text = list(text)
    # Check if each element of string is equidistant from the center (len(text) / 2)
    return all(text[i] == text[len(text) // 2 - i] for i in range(len(text) // 2))