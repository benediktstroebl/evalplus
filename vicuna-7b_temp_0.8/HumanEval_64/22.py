
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
    # Check if the string is empty
    if not s:
        return 0

    # Initialize the count of vowels
    vowel_count = 0

    # Iterate over all characters in the string
    for char in s:
        # Check if the character is a vowel
        if char in "aeiou":
            vowel_count += 1

    # Check if the last character is 'y' and increment the count if it is
    if s[-1] == "y":
        vowel_count += 1

    return vowel_count
