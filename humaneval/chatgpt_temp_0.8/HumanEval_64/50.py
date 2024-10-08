# CANNOT PARSE
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
    >>> vowels_count("aeiou")
    5
    >>> vowels_count("xyz")
    0
    """
    count = 0
    vowels = {'a', 'e', 'i', 'o', 'u'}
    for i in range(len(s)):
        if s[i].lower() in vowels:
            count += 1
    if s[-1].lower() == 'y' and count > 0 and s[-2].lower() not in vowels:
        count += 1
    return count
