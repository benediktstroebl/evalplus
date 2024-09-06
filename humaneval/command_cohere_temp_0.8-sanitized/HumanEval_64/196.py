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

    # Calculate the length of the string
    string_length = len(s)

    # Initialize the count of vowels to 0
    vowel_count = 0

    # Iterate over each character in the string
    for i in range(string_length):
        # Check if the character is a vowel
        if s[i] in ["a", "e", "i", "o", "u", "y"] :
            # If the character is a vowel, increment the count
            vowel_count += 1
        # Check if the character is 'y' and it is the last character in the string
        elif s[i] == 'y' and i == string_length - 1:
            # If the character is 'y' and it is the last character in the string, increment the count
            vowel_count += 1

    # Return the count of vowels in the string
    return vowel_count