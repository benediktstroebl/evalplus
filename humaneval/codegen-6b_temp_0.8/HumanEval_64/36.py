
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
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    count, i = 0, 0
    s = s.lower()

    while i < len(s):
        if s[i] not in vowels:
            i += 1
        elif s[i] == 'y' and i != len(s)-1:
            i += 1
        else:
            count += 1
            i += 1
    return count
