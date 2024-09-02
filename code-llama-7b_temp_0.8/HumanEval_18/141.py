

def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    # how_many_times('a', 'b') # 0
    # how_many_times('abc', 'a') # 1
    # how_many_times('ababab', 'ab') # 3
    # how_many_times('ababab', 'aba') # 2
    # how_many_times('aaaaaaaa', 'aaa') # 4
    # how_many_times('aaaaaaaa', 'a') # 7
    # how_many_times('aaaaaaaa', 'aab') # 0
    # how_many_times('abab', 'aa') # 1
    # how_many_times('aaaaa', 'a') # 5
    # how_many_times('a', 'a') # 1
    # how_many_times('aba', 'aba') # 1
    # how_many_times('aaaaba', 'aaa') # 3
    # how_many_times('aaaa', 'aa') # 3
    # how_many_times('ababa', 'aba') # 1
    # how_many_times('abcabcabcabc', 'ab') # 4
    # how_many_times('abcbabcbacd', 'abc') # 3
    # how_many_times('abcabcabc', 'abc') # 3
    # how_many_times('abcabcabc', 'cd') # 0
    # how_many_times('1234567890', '6789') # 0
    # how_many_times('1234567890', '4567') # 2
    # how_many_times('abcabcabcabcabcabcabc', 'abc') # 6
    # how_many_times('ababcabcabc', 'abc') # 2
    # how_many_times('ababcabcabc', 'ab') # 3
    # how_many_times('abc', 'abc') # 1
    # how_many_times('abc', 'abcabcd') # 0
    # how_many_times('abc', 'abcabcabcabc') # 3
    #
