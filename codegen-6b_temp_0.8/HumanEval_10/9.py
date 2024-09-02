

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
    if not string:
        return string

    while True:
        # length of prefix
        len_prefix = 1

        # length of postfix
        len_postfix = 0

        # starting index of the palindromic suffix
        start_index = 0

        # ending index of the palindromic suffix
        end_index = len(string) - 1

        while start_index < end_index - len_prefix + 1:
            if is_palindrome(string[start_index:end_index+1]):
                len_postfix = end_index - start_index + 1
                break

            len_prefix += 1
            end_index -= 1

        if not len_postfix:
            break

        start_index -= 1

        # start index was increased one more iteration because we are not
        # starting from the first index, but from the previous index.
        start_index += 1

        # append the reverse of the string prefix to the palindromic suffix
        string = (string[:start_index] +
                  string[start_index:start_index+len_postfix][::-1] +
                  string[start_index+len_postfix:])

    return string

