
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
    count = 0
    i = -1
    vowels = "aeiou"
    while i > -len(s):
        if s[i] in vowels:
            count = count + 1
        if s[i] == 'y' and s[i-1] == 'a':
            count = count + 1
        i = i - 1
    return count
