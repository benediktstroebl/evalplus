
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
    vowels = ["a", "e", "i", "o", "u", "y"]
    result = 0
    i = 0
    while i < len(s):
        if s[i] in vowels:
            result += 1
        if s[i] == "y":
            if (i+1) == len(s):
                result += 1
        i += 1
    return result

