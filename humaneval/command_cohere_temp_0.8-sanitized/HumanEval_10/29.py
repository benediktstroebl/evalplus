def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string. """
    # Find the longest palindromic postfix of the beginning string
    palindrome_postfix = ''
    while string != string[::-1]:
        string = string[1:]
        palindrome_postfix += string[0]
    # Reverse the string prefix that comes before the palindromic suffix and append it to form the shortest palindrome
    reversed_prefix = palindrome_postfix[::-1]
    return f"{reversed_prefix}{palindrome_postfix}"