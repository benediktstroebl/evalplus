
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
    import re
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    number = 0
    for vowel in vowels:
        num = re.findall(vowel, s)
        if len(num) == 2:
            vowel = num[1][-1]
            if vowel == s[-1]:
                number += 1
    return number
