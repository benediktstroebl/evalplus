def is_palindrome(text: str):
    """
    Checks if given string is a palindrome
    :param text: string to be checked
    :return: boolean
    """
    # Convert string to list to allow iterating through reversed letter by letter
    temp_list = list(text)
    # Compare each character in text with its corresponding reversed character
    for i in range(len(temp_list)):
        if temp_list[i] != temp_list[~i%len(temp_list)]:
            return False
    return True