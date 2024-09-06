def is_palindrome(text: str):
    """
    Checks if given string is a palindrome
    :param text: String to be checked
    :return: True if string is palindrome, False otherwise
    """
    # Convert string to lowercase to handle case-insensitive palindromes
    text = text.lower()
    # Check if text is empty or has only 1 character, which is a palindrome
    if not text or len(text) == 1:
        return True
    # Check if text is not a palindrome by comparing characters from start and end
    # iterating through half of the text length to cover the entire text
    for i in range(len(text) // 2):
        if text[i] != text[-1 - i]:
            return False
    return True