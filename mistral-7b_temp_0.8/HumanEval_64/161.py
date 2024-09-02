
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
    vowels_count = 0
    if s in ("a", "e", "i", "o", "u"):
        return 1
    elif s in ("y", "Y"):
        if len(s) > 1:
            if s[1:] in ("a", "e", "i", "o", "u"):
                return 1
        else:
            return 1
    else:
        return 0
