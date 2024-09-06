

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
    #bfs
    if string == '':
        return ''
    possible_palindromes = []
    for i in range(len(string)):
        prefix = string[:i+1]
        suffix = string[i+1:]
        if is_palindrome(prefix) and is_palindrome(suffix):
            possible_palindromes.append((prefix, suffix))
    min_len = len(string)
    min_possible_palindromes = possible_palindromes[:]
    for palindrome in possible_palindromes:
        prefix, suffix = palindrome
        for i in range(len(string)):
            suffix_reverse = suffix[::-1]
            preceeding_string = string[:i]
            front_prefix = prefix[:len(preceeding_string)]
            front_suffix = suffix[len(preceeding_string):]
            if front_prefix == front_suffix and not is_palindrome(preceeding_string):
                new_suffix = suffix_reverse + front_prefix + suffix
                if len(new_suffix) < min_len:
                    min_len = len(new_suffix)
                    min_possible_palindromes = [(prefix, new_suffix)]
                elif len(new_suffix) == min_len:
                    min_possible_palindromes.append((prefix, new_suffix))
    palindrome_string = min_possible_palindromes[0][1]
    return palindrome_string

