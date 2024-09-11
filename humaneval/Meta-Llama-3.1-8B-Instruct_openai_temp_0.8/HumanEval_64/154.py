```python
def vowels_count(s):
    """
    Returns the number of vowels in the given string.

    Vowels are 'a', 'e', 'i', 'o', 'u'. 'Y' is also a vowel when it's at the end of the word.

    Args:
        s (str): The input string.

    Returns:
        int: The number of vowels in the string.
    """
    # Initialize a counter for vowels
    count = 0
    # Check if the last character is 'y' (considering 'y' as a vowel at the end of the word)
    if len(s) > 0 and s[-1].lower() == 'y':
        # Remove 'y' from the string
        s = s[:-1]
    # Iterate over each character in the string
    for char in s:
        # Check if the character is a vowel (in lower case for simplicity)
        if char.lower() in 'aeiou':
            # If it's a vowel, increment the counter
            count += 1
    # Return the total count of vowels
    return count

# Test cases
print(vowels_count("abcde"))  # Expected output: 2
print(vowels_count("ACEDY"))  # Expected output: 3
```

This script defines a function `vowels_count` that takes a string `s` as input and returns the number of vowels in the string. The function considers 'y' as a vowel only when it's at the end of the word. The script includes test cases to verify the function's correctness.