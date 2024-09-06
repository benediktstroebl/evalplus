
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

    # BEGIN
    # END

    # Write your code here
    n_vowels = 0
    # make list of all possible vowels
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']

    # loop through letters in the word
    for letter in s:
        # if letter in vowels
        if letter in vowels:
            n_vowels += 1

    return n_vowels

