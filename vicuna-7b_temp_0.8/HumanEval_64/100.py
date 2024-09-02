
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
    word_len = len(s)
    vowel_count = 0

    for i in range(word_len):
        if s[i] in vowels:
            vowel_count += 1
        elif s[i] == 'y' and i > 0 and s[i - 1] == 'a':
            vowel_count += 1
        elif s[i] == 'y' and i < word_len - 1 and s[i + 1] == 'a':
            vowel_count += 1

    return vowel_count
