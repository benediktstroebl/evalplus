
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
    # variable to store count of vowels
    vowels_count = 0
    # loop through given word
    for c in s:
        # check if c is vowel
        if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u':
            # increment count if True
            vowels_count += 1
        # if c is not a vowel, check if its the last letter of the word
        elif c == 'y' and s[-1] == 'y':
            # increment count if True
            vowels_count += 1
    # return count of vowels
    return vowels_count

