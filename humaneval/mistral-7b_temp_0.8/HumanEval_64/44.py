
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
    vowels_count = 0
    for letter in s:
        if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
            vowels_count += 1
        if letter == "y" and s[len(s) - 1] == "y":
            vowels_count += 1
    return vowels_count
