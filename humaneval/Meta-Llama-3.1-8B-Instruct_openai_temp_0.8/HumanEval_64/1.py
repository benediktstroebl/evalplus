```python
def vowels_count(s):
    """
    Counts the number of vowels in a given string.

    Vowels are 'a', 'e', 'i', 'o', 'u'. 'y' is a vowel if it's at the end of the string.

    Parameters:
    s (str): The input string.

    Returns:
    int: The number of vowels in the string.
    """
    # Convert the string to lowercase for simplicity
    s = s.lower()
    
    # Initialize a counter for vowels
    count = 0
    
    # Iterate over each character in the string
    for char in s:
        # Check if the character is a vowel
        if char in 'aeiou':
            # If it's a vowel, increment the counter
            count += 1
        elif char == 'y' and s.endswith(char):
            # If it's 'y' and it's at the end of the string, increment the counter
            count += 1
    
    # Return the count of vowels
    return count

# Test cases
print(vowels_count("abcde"))  # Expected output: 2
print(vowels_count("ACEDY"))  # Expected output: 3
```

This script defines a function `vowels_count` that takes a string as input and returns the number of vowels in the string, following the given rules. It then includes test cases to demonstrate the function's correctness.