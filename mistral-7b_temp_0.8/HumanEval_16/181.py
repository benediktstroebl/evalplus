

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # write your code here
    if string == '':
        return 0
    else:
        alph = {}
        for x in string:
            if x in alph.keys():
                alph[x] += 1
            else:
                alph[x] = 1
        count = 0
        for x in alph:
            if alph[x] == 1:
                count += 1
        return count
