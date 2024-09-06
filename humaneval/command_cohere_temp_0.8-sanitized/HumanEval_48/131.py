def is_palindrome(text: str) -> bool:
    """
    Checks if a given string is a palindrome.
    """
    # Split the text into individual characters and reverse the list.
    char_list = list(text)
    char_list.reverse()
    # Join the characters back into a single string.
    reversed_text = ''.join(char_list)
    # Return True if the original and reversed strings are the same, otherwise False.
    return text == reversed_text