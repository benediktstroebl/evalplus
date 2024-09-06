def is_palindrome(text: str) -> bool:
    """
    Checks if a given string is a palindrome.
    """
    # Split the text into individual characters and reverse the list.
    char_list = list(text)
    reversed_list = char_list[::-1]
    
    # Check if the original text and the reversed text are the same
    return text == ''.join(reversed_list)