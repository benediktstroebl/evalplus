def is_palindrome(text: str):
    """
    Checks if given string is a palindrome
    :param text: string to be checked
    :return: boolean
    """
    # Convert string to list to allow iterating through reversed text
    text_list = list(text)
    # Compare each character in text to it's reverse (mirror image)
    return text_list == text_list[::-1]