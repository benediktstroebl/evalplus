
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
    vowels = {"a", "e", "i", "o", "u"}
    num_vowels = 0
    for i in range(len(s)):
        if s[i] in vowels:
            num_vowels += 1
    if s[-1] == "y":
        num_vowels -= 1
    return num_vowels
