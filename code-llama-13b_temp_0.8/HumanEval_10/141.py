

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

    # edge case
    if not string:
        return ''

    # count how many letters from the end we need to check
    # (this way we don't need to create additional copies of the string)
    for index in reversed(range(len(string))):
        if is_palindrome(string[index:]):
            break

    # find the longest postfix that is a palindrome, remember its start index
    palindrome_start_index = index

    # find the first letter before palindrome_start_index that is different than the one
    # after the palindrome, this letter is the first one we need to reverse
    for index in reversed(range(palindrome_start_index)):
        if string[index] != string[palindrome_start_index - index]:
            palindrome_start_index = index
            break

    # reverse chars before palindrome_start_index
    return string[:palindrome_start_index] + string[palindrome_start_index:][::-1]

