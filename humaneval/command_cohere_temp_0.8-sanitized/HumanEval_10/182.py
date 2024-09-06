def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]
def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string. """
    if not string:
        return string

    # Find the index of the last palindromic character
    right_edge = len(string) - 1
    while not is_palindrome(string[right_edge:]):
        right_edge -= 1

    # Extend the palindrome to the right
    max_length = right_edge + 1
    while right_edge >= 0 and not is_palindrome(string[right_edge:max_length]):
        right_edge -= 1
        max_length = right_edge + 1

    # Extend the palindrome to the left
    left_edge = 0
    while not is_palindrome(string[left_edge:max_length]):
        left_edge += 1

    # Reverse the middle part and return the palindrome
    return string[:left_edge] + string[right_edge:max_length][::-1] + string[left_edge+max_length:]