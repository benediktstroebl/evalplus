
FIX = """
Add more test cases.
"""

def vowels_count(s):
    """Write a function vowels_count which takes a string representing
    a word as input and returns the number of vowels in the string.
    Vowels in this case are 'a', 'e', 'i', 'o', 'u'. Here, 'y' is also a
    vowel, but only when it is at the end of the given word.

    Example:
    >>> vowels_count("abcde")
    2
    >>> vowels_count("ACEDY")
    3
    """
    a = 0
    e = 0
    i = 0
    o = 0
    u = 0
    y = 0

    for x in s:
        if x == 'a':
            a += 1
        elif x == 'e':
            e += 1
        elif x == 'i':
            i += 1
        elif x == 'o':
            o += 1
        elif x == 'u':
            u += 1
        elif x == 'y' and len(s) == len(s.rstrip('y')):
            y += 1

    return a + e + i + o + u + y
