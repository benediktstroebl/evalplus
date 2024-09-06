def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]
def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string. """
    # Find the position of the last palindrome suffix in the string
    n = len(string)
    for i in range(n, 0, -1):
        if is_palindrome(string[i-1:i+i]):
            break

    # Reverse the string from 0 to i and append it to the end to form a palindrome
    result = string[:i] + string[i:][::-1]
    return result