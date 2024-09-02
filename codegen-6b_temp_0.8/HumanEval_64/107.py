
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
    num_vowels = 0
    for letter in s:
        if letter in VOWELS:
            num_vowels += 1

    if not s or s == '':
        return 0
    # elif s[-1] in VOWELS:
    #     return 1 + vowels_count(s[:-1])
    else:
        return num_vowels


