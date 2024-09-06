def is_palindrome(text: str):
    """
    Checks if given string is a palindrome
    :param text: string to be checked
    :return: True if string is palindrome, False otherwise
    """
    # Convert string to lowercase to handle case-insensitive palindromes
    text = text.lower()
    # Check if text is empty or has only 1 character, which is trivial palindromes
    if not text or len(text) == 1:
        return True
    # Check if text is a palindrome by comparing characters from beginning and end
    for i in range(len(text) // 2):
        if text[i] != text[-1-i]:
            return False
    return True