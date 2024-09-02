

def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """
    if not string:
        return 0
    else:
        substring_size = len(substring)
        counter = 0
        i = 0
        while i <= len(string) - substring_size:
            if string[i] == substring[0]:
                j = 1
                while substring[j] == string[i+j]:
                    j += 1
                    if j == substring_size:
                        counter += 1
                        i += j-1
                        break
                i += 1
            else:
                i += 1
        return counter
