
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    # check input
    if not isinstance(s, str):
        raise TypeError('Input must be a string')
    
    # setup counter
    counter = 0
    
    # go through string
    for i, letter in enumerate(s):
        if i % 2 == 0:
            if letter.isupper():
                counter += 1
    
    return counter
