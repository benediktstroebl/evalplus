

def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    
    # make sure that the substring is smaller than the string
    if len(substring) > len(string):
        return 0
    
    # make sure that the substring is contained in the string
    if substring not in string:
        return 0

    # find the length of the substring in the string
    sub_len = len(substring)
    
    # find how many full substring there are
    full_substr_n = int(len(string) / sub_len)
    
    # find the last substring
    last_substr = string[-sub_len:]
    
    # if the last substring is identical to the substring, count it in
    if last_substr == substring:
        full_substr_n += 1
        
    return full_substr_n
