
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
    word_split = set()
    word_split.add('a')
    word_split.add('e')
    word_split.add('i')
    word_split.add('o')
    word_split.add('u')
    for char in s:
        if char in word_split:
            word_split.remove(char)
    return len(word_split)
