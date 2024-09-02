

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
    # Define a list of all possible characters
    chars = 'abcdefghijklmnopqrstuvwxyz'
    # Define a dictionary of characters with frequency counts
    freq = Counter(chars)
    # Find the longest postfix of the string that is a palindrome
    prefix = []
    for char in string:
        if is_palindrome(char):
            prefix.append(char)
            freq[char] += 1
            if len(prefix) > len(string):
                prefix = string[prefix[::-1]]
    # Append the reverse of the prefix to the end of the string
    if prefix:
        string = string + prefix[::-1]
    return string

