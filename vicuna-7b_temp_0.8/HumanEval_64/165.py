
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
    vowels = 'aeiou'
    vowel_end = 'y' if len(s) > 1 else False
    return sum(s.count(v) for v in vowels if vowels.count(v) > 0 if vowels.count(v) > 0 and vowels.count(v) > 0 and vowels.count(v) > 0 or vowels.count(v) > 0 and vowel_end)
