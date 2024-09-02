
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
    """
    # Method 1
    num_vowels = 0
    for c in s:
        if c in ('a', 'e', 'i', 'o', 'u', 'y'):
            num_vowels += 1
    return num_vowels

    # Method 2
    return sum(c in ('a', 'e', 'i', 'o', 'u', 'y') for c in s)
    """
    # Method 3
    count = 0
    for c in s:
        if c in ('a', 'e', 'i', 'o', 'u', 'y'):
            count += 1
    return count

