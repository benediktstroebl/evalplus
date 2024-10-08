# CANNOT PARSE
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
    >>> vowels_count("hello")
    2
    >>> vowels_count("strengths")
    1
    >>> vowels_count("Python")
    1
    """
    vowels = 'aeiouy'
    count = 0
    if s[-1] in vowels:
        for i in range(len(s)-1):
            if s[i].lower() in vowels:
                count += 1
        count += 1
    else:
        for char in s:
            if char.lower() in vowels:
                count += 1
    return count
