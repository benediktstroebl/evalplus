
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
    if not s:
        return 0
    count = 0
    for i, v in enumerate(s):
        if v in ['a', 'e', 'i', 'o', 'u', 'y']:
            count += 1
            if i == len(s) - 1 and v == 'y':
                count -= 1
    return count

