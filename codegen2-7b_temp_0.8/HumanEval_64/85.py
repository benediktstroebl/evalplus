
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
    for ch in s:
        if ch == "a" or ch == "e" or ch == "i" or ch == "o" or ch == "u":
            vowels += 1
    vowels += 1 if s[-1] == "y" else 0
    return vow
