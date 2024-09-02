
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
    for i in s:
        if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
            vowels_count += 1
        elif i == "y":
            if (s[len(s)-1] == "a" or s[len(s)-1] == "e" or s[len(s)-1] == "i" or s[len(s)-1] == "o" or s[len(s)-1] == "u"):
                vowels_count += 1
    return vowels
