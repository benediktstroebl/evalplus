def is_palindrome(text: str) -> bool:
    """
    Checks if a given string is a palindrome.
    """
    # Split the text into individual characters and reverse the list.
    char_list = list(text)
    char_list.reverse()
    # Iterate through the characters of the original text and the reversed text to check if they are the same
    return text == ''.join(char_list)