
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
    s = s.lower()
    if s[-1] == 'y':
        if s[-2] in ['a','e','i','o','u']:
            return s.count('y') + s.count('a') + s.count('e') + s.count('i') + s.count('o') + s.count('u') - 1
        return s.count('y')
    return s.count('a') + s.count('e') + s.count('i') + s.count('o') + s.count('u')

