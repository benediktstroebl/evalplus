

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
    # Find the longest postfix of supplied string that is a palindrome
    # Palindromic suffix
    palindromic_suffix = ''
    reversed_string = string[::-1]
    # Initialize position of palindromic suffix at the end of the reversed string
    # len(reversed_string) will be the length of the palindrome suffix
    position_of_palindrome_suffix = len(reversed_string)
    while position_of_palindrome_suffix > 0:
        # Loop until palindromic suffix is at the beginning of the reversed string
        # Find the first 0 from the right
        position = -1
        # Take the last character of palindromic suffix
        last_char = palindromic_suffix[position_of_palindrome_suffix]
        while position < position_of_palindrome_suffix - 1 and last_char == reversed_string[position]:
            position += 1
        position_of_palindrome_suffix = position
        palindromic_suffix = palindromic_suffix + last_char
    # Odd-length palindrome suffix goes to the end of the reversed string
    # Even-length palindrome suffix
    # Simple count based solution with O(n) running time complexity
    # Find the last odd-length non-palindromic character
    position = 0
    while position < len(string):
        if string[position] not in palindromic_suffix:
            position += 1
        else:
            break
    if position == len(string):
        # No non-palindromic characters were found
        return string
    # Choose the palindromic suffix between position and the position of the non-palindromic character
    palindrome_suffix = string[position:]
    # Append to the end of the reversed string the suffix with the palindromic suffix
    # Reverse the suffix of the reversed string
    palindrome_suffix = palindrome_suffix[::-1]
    return reversed_string + palindrome_suffix
