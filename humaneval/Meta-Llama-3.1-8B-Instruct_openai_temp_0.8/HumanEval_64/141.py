```python
# Define the set of vowels and the 'y' condition
VOWELS = {'a', 'e', 'i', 'o', 'u'}
END_WITH_Y = {'y'}

def vowels_count(s):
    """
    Returns the number of vowels in the given string.
    'y' is considered a vowel only when the string ends with 'y'.

    Args:
        s (str): A string representing a word.

    Returns:
        int: The number of vowels in the string.
    """
    # Convert the string to lowercase for simplicity
    s = s.lower()
    
    # Initialize a counter for vowels
    count = 0
    
    # Check if the string ends with 'y'
    ends_with_y = s.endswith('y')
    
    # Iterate over each character in the string
    for char in s:
        # If the character is a vowel, increment the counter
        if (char in VOWELS) or (char in END_WITH_Y and ends_with_y):
            count += 1
    
    # Return the total count of vowels
    return count

# Test cases
print(vowels_count("abcde"))  # Expected output: 2
print(vowels_count("ACEDY"))  # Expected output: 3
print(vowels_count("hello"))  # Expected output: 2
print(vowels_count("aeiou"))  # Expected output: 5
print(vowels_count("bcdfg"))  # Expected output: 0
```

This script defines a function `vowels_count` that takes a string as input and returns the number of vowels in the string, considering 'y' as a vowel only when the string ends with 'y'. The function uses a set to store the vowels for efficient lookups. The test cases at the end demonstrate the function's correctness.