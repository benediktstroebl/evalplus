

def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]


def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string.
    Algorithm idea is simple:
    - Find the longest postfix of supplied string that is a palindrome.
    - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    >>> make_palindrome('')
    ''
    >>> make_palindrome('cat')
    'catac'
    >>> make_palindrome('cata')
    'catac'
    """
    string = string.lower()
    # Splits string into two parts and tries to find palindrome in the second part
    # If the string is not palindrome, it finds palindrome in the first part
    # And append it to the second part with reversed first part
    # The last condition is added to handle the case when given string is already palindrome
    while len(string) > 1:
        first_part = string[:len(string) // 2]
        second_part = string[len(string) // 2:]
        if is_palindrome(second_part):
            return second_part + first_part[::-1]
        else:
            string = first_part + second_part[::-1]
    return string

