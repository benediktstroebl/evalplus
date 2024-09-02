
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
    vow = "aeiou"
    count = 0
    l = len(s)
    for i in range(l):
        if s[i] in vow:
            count += 1
        elif s[i] == 'y' and s[i-1] not in vow:
            count += 1
    return count
