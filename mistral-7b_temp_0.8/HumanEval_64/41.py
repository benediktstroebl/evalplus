
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

    # YOUR CODE HERE
    vowels = 0
    vowels_list = ['a', 'e', 'i', 'o', 'u', 'y']
    for letter in s:
        if letter in vowels_list:
            vowels += 1
        elif s[-1] == 'y':
            if letter == 'y':
                vowels += 1
    return vowels
