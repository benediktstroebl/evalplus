def vowels_count(s):
    """
    This function counts the number of vowels in a given string.
    Special case: 'y' is treated as a vowel only at the end of a word.

    Args:
        s (str): The input word.

    Returns:
        int: The number of vowels in the word.
    """
    # Define the vowels and the special case 'y'
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    count_vowels = 0

    # Loop through each char in the string
    for char in s:
        # Check if the current char is a vowel (or 'y' at the end of a word)
        if char in vowels or (s[-1] == 'y' and char == 'y'):
            count_vowels += 1

    return count_vowels