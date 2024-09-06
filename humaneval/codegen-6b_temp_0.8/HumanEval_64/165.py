
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
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowel_count = 0

    for letter in s:
        if letter in vowels:
            vowel_count += 1

    for i in range(len(s) - 1, -1, -1):
        if s[i] in vowels:
            vowel_count += 1

    return vowel_count

