def is_palindrome(text: str) -> bool:
    """
    Checks if a given string is a palindrome.
    """
    # Convert string to list to allow index-based traversal
    text = list(text)
    # Traverse the list from both ends towards the middle
    for i in range(len(text) // 2):
        # If characters at corresponding positions are not equal, it's not a palindrome
        if text[i] != text[-1-i]:
            return False
    return True