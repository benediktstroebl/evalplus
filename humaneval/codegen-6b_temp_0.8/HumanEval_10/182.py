

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
    # end_pos = find_longest_palindrome(string)
    # suffix = string[end_pos:len(string):]
    # seq = string[:end_pos:][::-1]
    # result = string + suffix + seq
    # return result
    # Using the start and end indexes of a string to slice and reverse the string
    # alist = list(string)
    # sl = slice(start, end)
    # alist[sl] = alist[sl][::-1]
    # result = ''.join(alist)
    # return result
    # 
    # 
    # 
    # 
    # 
    # 
    # 
    # 
    # 
    # 
    # 
    # 
    # 
    # end_pos = find_longest_palindrome(string)
    # suffix = string[end_pos:len(string):]
    # seq = string[:end_pos:][::-1]
    # result = string + suffix + seq
    # return result
    # temp = string[start:end]
    # temp = temp[::-1]
    # start -= 1
    # result = [start, end]
    # return result
    # 
    # 
    # 
    # 
    # 
    # 
    # 
    # 
    # 
    # 
    # 
    # 
    # 
    # 
    # 
    # 
    # 
    # 
    # 
    # 
    # 
    # 
    # 
    # 
    # 
    # 
    # 
    # 
    # 
    # 
    # 
    # 
    # 
    # 
    # 
    # 
    # 
    # 
    # 
    # 
    # 
    # 
    # 
    # 
    # 
    # 
    # 
    # 
    # 
    # 
    # 
    # 
    # 
