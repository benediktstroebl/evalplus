```python
def vowels_count(s):
    """
    Count the number of vowels in a given string.

    Vowels are 'a', 'e', 'i', 'o', 'u'. 'y' is also a vowel if it's at the end of the string.

    Args:
        s (str): The input string.

    Returns:
        int: The number of vowels in the string.
    """
    # Convert the string to lowercase to simplify the vowel check
    s = s.lower()
    
    # Initialize a counter for the number of vowels
    count = 0
    
    # Check each character in the string
    for i, char in enumerate(s):
        # Check if the character is a vowel
        if char in 'aeiou':
            count += 1
        # If the character is 'y' and it's at the end of the string, count it as a vowel
        elif char == 'y' and i == len(s) - 1:
            count += 1
    
    # Return the total count of vowels
    return count

# Example usage:
print(vowels_count("abcde"))  # Output: 2
print(vowels_count("ACEDY"))  # Output: 3
print(vowels_count("hello"))  # Output: 2
print(vowels_count("world"))  # Output: 1
print(vowels_count("python")) # Output: 2
```

This script defines a function `vowels_count` that takes a string as input and returns the number of vowels in the string, according to the specified rules. The example usage at the end demonstrates how to use the function with different inputs.