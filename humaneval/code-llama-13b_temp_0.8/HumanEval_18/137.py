

def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """

    if string == "":
        return 0
    
    if len(string) < len(substring):
        return 0
    
    count = 0
    i = 0

    while i < len(string):

        if string[i] == substring[0]:
            aux = i
            found = True
            j = 0
            while found and j < len(substring):
                if string[aux] == substring[j]:
                    aux += 1
                    j += 1
                else:
                    found = False

            if found:
                count += 1
                i = aux

        i += 1
    return count

