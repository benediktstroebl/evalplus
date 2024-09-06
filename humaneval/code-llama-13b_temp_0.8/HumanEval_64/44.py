
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
    if not isinstance(s, str):
        raise TypeError("Input must be a string")

    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    vowels_count = 0

    for ch in s.lower():
        if ch in vowels:
            vowels_count += 1

    return vowels_count
