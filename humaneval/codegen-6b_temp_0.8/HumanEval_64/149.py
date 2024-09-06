
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
    vowels = {'a':0, 'e':0, 'i':0, 'o':0, 'u':0, 'y':0}
    for letter in s.lower():
        if letter in vowels:
            vowels[letter] += 1
    return sum(vowels.values())
