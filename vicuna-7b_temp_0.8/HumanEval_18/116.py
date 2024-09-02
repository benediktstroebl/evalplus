

def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    n = 0
    start = 0
    end = 0
    
    for i in range(len(string)):
        if string[i:i+1] == substring:
            start = i
            end = i
        
        if start != 0:
            n += 1
            end = start - 1
    
    return n

string1 = "abcdefg"
string2 = "abc"
