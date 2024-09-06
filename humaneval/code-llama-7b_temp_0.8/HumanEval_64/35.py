
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
    # check the solution
    if "y" not in s:
        return sum([s.count(i) for i in ['a', 'e', 'i', 'o', 'u']])
    else:
        # the last 'y' in the string is a vowel
        return sum([s[:-1].count(i) for i in ['a', 'e', 'i', 'o', 'u']]) + 1
