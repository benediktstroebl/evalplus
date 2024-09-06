

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
    def find_long_palindrome(string: str, start: int, end: int) -> (int, int):
        # Find the longest palindrome that starts at `start` and ends at `end`.
        while start >= 0 and end <= len(string) and string[start] == string[end - 1]:
            start -= 1
            end += 1
        return (start, end - 1)

    if is_palindrome(string):
        return string

    longest_palindrome_start = 0
    longest_palindrome_end = 1
    for i in range(len(string)):
        # search for longest palindrome
        (start, end) = find_long_palindrome(string, i, i + 1)
        (new_start, new_end) = find_long_palindrome(string, i, i + 2)
        if end - start > longest_palindrome_end - longest_palindrome_start:
            longest_palindrome_start = start
            longest_palindrome_end = end
        if new_end - new_start > longest_palindrome_end - longest_palindrome_start:
            longest_palindrome_start = new_start
            longest_palindrome_end = new_end

    return string[0:longest_palindrome_start] + string[longest_palindrome_end:][::-1]
