
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

    vowels = 0

    if len(s) > 0:
        if s[0] == 'a':
            vowels += 1
        elif s[0] == 'e':
            vowels += 1
        elif s[0] == 'i':
            vowels += 1
        elif s[0] == 'o':
            vowels += 1
        elif s[0] == 'u':
            vowels += 1

    for c in s[1:]:
        if c == 'a':
            vowels += 1
        elif c == 'e':
            vowels += 1
        elif c == 'i':
            vowels += 1
        elif c == 'o':
            vowels += 1
        elif c == 'u':
            vowels += 1
        elif c == 'y':
            vowels += 1

    return vowels
