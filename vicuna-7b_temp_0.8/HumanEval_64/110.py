
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
    # Letters that are not vowels:
    non_vowels = 'bcdfghjklmnpqrstvwxyz'

    # Find the length of the string
    s_len = len(s)

    # Initialize the count of vowels to 0
    vowel_count = 0

    # Iterate over each character in the string
    for char in s:
        # Check if the character is a vowel
        if char in vowels:
            # If it is a vowel, increment the vowel count
            vowel_count += 1
        # If it is not a vowel, check if it is a non-vowel
        elif char not in non_vowels:
            # If it is a non-vowel, increment the count of non-vowels
            non_vowel_count += 1

    # Return the count of vowels
    return vowel_count
