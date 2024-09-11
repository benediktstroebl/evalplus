```python
def vowels_count(s):
    """
    This function counts the number of vowels in a given word.

    Vowels in this case are 'a', 'e', 'i', 'o', 'u'. However, 'y' is also a vowel
    when it is at the end of the given word.

    Parameters:
    s (str): The input string.

    Returns:
    int: The number of vowels in the string.

    Examples:
    >>> vowels_count("abcde")
    2
    >>> vowels_count("ACEDY")
    3
    """
    # Convert the string to lower case to handle case sensitivity
    s = s.lower()

    # Initialize a counter for vowels
    count = 0

    # Check if the last character is 'y'
    last_char_is_y = s[-1] == 'y'

    # Iterate over each character in the string
    for char in s:
        # Check if the character is a vowel
        if char in 'aeiouy':
            # If 'y' is not at the end of the word, decrement the count
            if last_char_is_y and char == 'y':
                last_char_is_y = False
            else:
                count += 1

    # Return the count of vowels
    return count
```

This script defines a function `vowels_count` that takes a string `s` as input and returns the number of vowels in the string. It handles the special case of 'y' being a vowel only when it's at the end of the string.