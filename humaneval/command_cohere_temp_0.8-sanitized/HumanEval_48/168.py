def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome
    :param text: string to be checked
    :return: boolean -- True if it is a palindrome, False otherwise
    """
    # Convert text to lowercase to handle case-insensitive palindromes
    text = text.lower()
    # Check if text is an empty string
    if not text:
        return True
    # Check if text is a palindrome by comparing characters from beginning and end
    return text[0:] == text[::-1]