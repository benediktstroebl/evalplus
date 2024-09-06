
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

    def is_vowel(s):
        if s.lower() in "aeiouy":
            return s
        return None

    def is_last_vowel(s):
        if s.lower() in "aeiouy":
            return s
        return None

    count = 0
    for c in s:
        if is_vowel(c) is not None:
            count += 1
    return count

