
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
    # Use a dictionary to store the frequency of each vowel.
    vowels = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    vowel_count = 0
    for char in s:
        if char in vowels:
            vowels[char] += 1
        else:
            vowel_count += 1
    return vowel_count

