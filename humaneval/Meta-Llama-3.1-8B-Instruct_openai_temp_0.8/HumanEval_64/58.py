### Vowels Count Function
```python
def vowels_count(s):
    """
    This function takes a string representing a word as input and returns
    the number of vowels in the string. Vowels are 'a', 'e', 'i', 'o', 'u'.
    'y' is also a vowel, but only when it is at the end of the given word.

    Args:
        s (str): The input string.

    Returns:
        int: The number of vowels in the string.
    """

    # Convert the string to lowercase to simplify vowel checking
    s = s.lower()

    # Initialize a counter for vowels
    count = 0

    # Check if the last character is 'y'
    is_last_char_y = len(s) > 1 and s[-1] == 'y'

    # Iterate over each character in the string
    for char in s:
        # Check if the character is a vowel
        if char in 'aeiou' or (char == 'y' and is_last_char_y):
            # If it is, increment the vowel counter
            count += 1

    # Return the total count of vowels
    return count

# Example use cases
print(vowels_count("abcde"))  # Output: 2
print(vowels_count("ACEDY"))  # Output: 3
```
This Python script defines the `vowels_count` function as per the given requirements and provides example use cases to demonstrate its functionality.