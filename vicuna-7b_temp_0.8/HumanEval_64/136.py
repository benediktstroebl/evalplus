
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
    # Get all the characters in the string
    characters = set(s)

    # Get all the vowels
    vowels = "aeiou"

    # Create a set of all the characters in the vowels
    vowel_set = set(vowels)

    # Create a set of all the characters in the string except the vowels
    non_vowels = characters - vowel_set

    # Check if the string has any vowels
    if len(non_vowels) == 0:
        return len(vowel_set)

    # Add up the number of vowels
    vowel_count = 0
    for char in non_vowels:
        vowel_count += 1

    # Return the result
    return vowel_count
