

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
    # 将字符串分割为左右两半
    length = len(string) // 2
    half_left = string[:length]
    half_right = string[length:]
    
    # 搜索最长带有轮廓化字符的后缀
    while half_left[-1] == half_left[-2][::-1]:
        half_left = half_left[:-1]
        half_left_palindrome = half_left + half_left[:-1].count(half_left[-1])
        half_right = half_right[:-1]
        half_right_palindrome = half_right + half_right[:-1].count(half_right[-1])
        if len(half_left_palindrome) > len(half_right_palindrome):
            return half_left_palindrome
        
    # 如果找不到，那么使用默认值
    return string

