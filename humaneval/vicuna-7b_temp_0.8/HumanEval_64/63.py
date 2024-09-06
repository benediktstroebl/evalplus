
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
    # Create a list of strings with the vowels
    vowels = "aeiou"

    # Create a set of strings with the vowels
    vowel_set = set(vowels)

    # Create an empty list to store the vowel count
    vowel_count = []

    # Iterate through the characters of the string
    for c in s:
        # If the character is a vowel
        if c in vowel_set:
            # Add 1 to the vowel count
            vowel_count.append(1)

            # If the character is 'y' and it's at the end of the word
            if c == "y" and s.endswith(c):
                # Add 1 to the vowel count
                vowel_count.append(1)

        # If the character is not a vowel
        elif c not in vowel_set:
            # Add 1 to the vowel count
            vowel_count.append(1)

    # Return the vowel count
    return len(vowel_count)
