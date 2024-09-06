
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
    vowels = set(('a','e','i','o','u','y'))
    vowels_in_word = set()
    for c in s:
        if c in vowels:
            vowels_in_word.add(c)
    if 'y' in vowels_in_word:
        vowels_in_word.remove('y')
    return len(vowels_in_word)
