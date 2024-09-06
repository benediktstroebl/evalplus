def is_palindrome(text: str):
    """
    Checks if given string is a palindrome
    :param text: string to be checked
    :return: boolean
    """
    # Convert string to list to allow iterating through reversed text
    text_list = list(text)
    # Compare each character of text with reversed char at same index
    for i in range(len(text)):
        if text_list[i] != text_list[~i]:  # Use ~i to get index of reversed order
            return False
    return True