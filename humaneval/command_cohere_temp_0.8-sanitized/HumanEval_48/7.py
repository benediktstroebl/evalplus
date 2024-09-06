def is_palindrome(text: str) -> bool:
    """
    Checks if a given string is a palindrome.
    """
    # Split the text into individual characters and reverse the list.
    char_list = list(text)
    reversed_char_list = char_list[::-1]
    
    # Compare the original text with its reverse to determine if it's a palindrome
    return text == ''.join(reversed_char_list)