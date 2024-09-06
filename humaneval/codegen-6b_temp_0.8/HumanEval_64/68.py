
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
    vowels = set("aeiouy")
    count = 0
    if s == "":
        return 0
    if s[-1] in vowels:
        count += 1
    for i in range(len(s) -1, -1, -1):
        if s[i] in vowels:
            count += 1
            break
    return count
