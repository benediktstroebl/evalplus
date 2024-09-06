def vowels_count(s):
    """
    This function counts the number of vowels in a given string.
    Specifically, it counts 'a', 'e', 'i', 'o', 'u', and 'y' as vowels,
    but only when 'y' is at the end of the word.

    Args:
        s (str): The input string to count vowels in.

    Returns:
        int: The number of vowels in the string.
    """

    # Define the vowels that are to be counted
    vowels = set(['a', 'e', 'i', 'o', 'u', 'y'])

    # Ensure the input is a string
    if not isinstance(s, str):
        raise ValueError("Input must be a string")

    # Initialize the count of vowels to zero
    count = 0

    # Iterate over each character in the string
    for char in s:
        # Check if the character is a vowel (or 'y' at the end of the word)
        if char in vowels or (char == 'y' and s[-1] == char):
            count += 1

    return count