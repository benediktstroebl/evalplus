
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
    # Keep a count of vowels.
    vowels = 0
    # If the string is empty or a single vowel, return 1.
    if not s or len(s) == 1:
        return 1
    else:
        # Check if the string is a single vowel followed by 'y'.
        if s[-1] == 'y' and len(s) == 2:
            return 1
        # Iterate over the characters in the string.
        for c in s:
            if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u':
                vowels += 1
        return vowels

