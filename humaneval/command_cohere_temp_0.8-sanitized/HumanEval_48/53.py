def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome
    :param text: string to be checked
    :return: boolean -- True if input is palindrome, else False
    """
    # Convert text to lowercase to handle case-insensitive palindromes
    text = text.lower()
    # Check if text is an empty string or has only 1 character
    if len(text) < 2:
        return True
    # Split the text into two halves
    mid = len(text) // 2
    left, right = text[:mid], text[mid:]
    # Check if left and right halves are equal
    return left == right