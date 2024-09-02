

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

    def find_longest_palindromic_postfix(string: str) -> str:
        longest_palindrome_start_idx = 0
        longest_palindrome_len = 0
        for idx in range(len(string)):
            # Expand in both directions and check if we have a palindrome
            # For each expansion we can check only 2 letters, which makes our time complexity linear
            left_idx = idx
            right_idx = idx
            while left_idx >= 0 and right_idx < len(string) and string[left_idx] == string[right_idx]:
                # Found palindrome candidate
                if right_idx - left_idx + 1 > longest_palindrome_len:
                    longest_palindrome_start_idx = left_idx
                    longest_palindrome_len = right_idx - left_idx + 1
                left_idx -= 1
                right_idx += 1
        return string[longest_palindrome_start_idx:longest_palindrome_start_idx + longest_palindrome_len]

    palindromic_postfix = find_longest_palindromic_postfix(string)
    return string + palindromic_postfix[::-1]

