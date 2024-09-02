
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

    # Create a list of words in the string
    words = s.split()

    # Initialize a variable to store the count of vowels
    vowel_count = 0

    # Iterate through each word in the list
    for word in words:
        # Check if the word ends with 'y' and it is not the first word
        if word[-1] == 'y' and word != s[:1]:
            # Increment the count of vowels if the word is a vowel
            if word.lower() in "aeiou":
                vowel_count += 1
            else:
                # Reset the count of vowels if the word is not a vowel
                vowel_count = 0

    # Return the count of vowels
    return vowel_count
