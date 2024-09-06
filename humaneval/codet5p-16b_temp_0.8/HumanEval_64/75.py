
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

    assert s, "The given string is empty!"

    vowels = "aeiou"
    count = 0

    if s[0] in vowels:
        count += 1

    for i in range(1, len(s)):
        if s[i] in vowels:
            count += 1

        if s[i - 1] in vowels and s[i] in vowels:
            count -= 1

    if s[-1] in vowels:
        count += 1

    return count
