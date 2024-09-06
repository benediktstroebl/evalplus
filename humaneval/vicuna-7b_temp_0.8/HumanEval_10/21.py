

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
    start = 0
    end = 0
    while end < len(string):
        if is_palindrome(string[start:end]) and string[start:end] != string[end:start]:
            result = string[start:end]
            while is_palindrome(result[::-1]) or end - result.find(result[::-1]) == len(result) - len(result[::-1]):
                end += 1
                result += string[start]
            return result
        end += 1
        start += 1
    return None

