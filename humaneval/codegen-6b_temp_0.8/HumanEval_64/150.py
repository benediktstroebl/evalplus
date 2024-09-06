
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
    vowels_look_up = {"a":1, "e":1, "i":1, "o":1, "u":1, "y":1}
    for c in s:
        vowels_look_up[c] = 1
        vowels += vowels_look_up[c]
    return vowels

