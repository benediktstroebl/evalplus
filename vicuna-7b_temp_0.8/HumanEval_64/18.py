
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
    # Check if the string is empty
    if not s:
        return 0

    # Check if the string is only one vowel
    if len(s) == 1:
        vowel = s[0]
        if vowel in ['a', 'e', 'i', 'o', 'u']:
            return 1

    # Initialize count to 0
    count = 0

    # Check for multiple vowels
    for char in s:
        if char in ['a', 'e', 'i', 'o', 'u']:
            count += 1

    # Check if 'y' is at the end of the given word
    if s[-1] == 'y':
        count += 1

    return count
