```python
def vowels_count(s):
    """
    This function takes a string representing a word as input and returns 
    the number of vowels in the string. Vowels in this case are 'a', 'e', 'i', 'o', 'u'. 
    Here, 'y' is also a vowel, but only when it is at the end of the given word.

    Parameters:
    s (str): The input string.

    Returns:
    int: The number of vowels in the input string.
    """

    # Convert the string to lower case to make the function case-insensitive
    s = s.lower()

    # Initialize a counter for vowels
    count = 0

    # Initialize a flag to check if 'y' is at the end of the word
    y_at_end = False

    # If the word ends with 'y', set the flag to True
    if s.endswith('y'):
        y_at_end = True
        # Remove the last character ('y') from the word
        s = s[:-1]

    # Count the vowels in the word
    for char in s:
        # If the character is a vowel or 'y' at the end of the word, increment the count
        if char in 'aeiou' or (char == 'y' and y_at_end):
            count += 1

    return count

# Test cases
print(vowels_count("abcde"))  # Expected output: 2
print(vowels_count("ACEDY"))  # Expected output: 3
```

This script defines a function `vowels_count` that takes a string as input and returns the number of vowels in the string. It handles the special case where 'y' is considered a vowel if it is at the end of the word. The function is case-insensitive and uses a flag to track whether 'y' is at the end of the word. The test cases are included at the bottom of the script.