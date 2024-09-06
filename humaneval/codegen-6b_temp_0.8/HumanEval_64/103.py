
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
    # Find all the vowels.
    v = [v for v in s if v in 'aeiou']
    vcount = len(v)
    # If there is at least one vowel at the end,
    # then count it as well as if the vowel is at the beginning.
    if v[-1] == s[0]:
        vcount += 1
    if v[0] == s[-1]:
        vcount += 1
    return vcount
