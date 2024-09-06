
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    # Hint:
    # a/A/A.lower() == 'a'
    # e/E/E.lower() == 'e'
    # i/I/I.lower() == 'i'
    # o/O/O.lower() == 'o'
    # u/U/U.lower() == 'u'
    # d/D/D.lower() == 'd'
    # B/b/B.lower() == 'b' - upper case comes first
    return sum(
        [
            1 if a.lower() in ('a', 'e', 'i', 'o', 'u') else 0
            for a in s[::2]
        ]
    )

