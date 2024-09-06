def is_palindrome(text: str):
    """
    Checks if a given string is a palindrome.
    """
    # Your code here. Make sure to test it with the provided test cases.
    return text == text[::-1]