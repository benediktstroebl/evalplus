

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
    string_len = len(string)
    # Step 1. Find the longest postfix of supplied string that is a palindrome.
    # We will have to examine all the possible substrings that may be a palindrome and pick the longest.
    # To skip all the substrings that can not be palindrome, we will have to skip all the strings that are not prefixes of the supplied string.
    for i in range(1, string_len + 1):
        # Skip prefixes of the string.
        if string[0:i] != string[-i:]:
            continue
        # Get a postfix starting at position i.
        postfix = string[i:]
        # Check if postfix is a palindrome.
        if is_palindrome(postfix):
            # If palindrome is found, then break and return it.
            return postfix
    # If we get here, that means that no palindrome was found. So, we will have to append palindrome that is reverse of the prefix.
    for i in range(1, string_len + 1):
       
