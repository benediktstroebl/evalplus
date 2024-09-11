### Vowels Count Script
```python
# Define the vowels as a set for efficient lookups
VOWELS = {'a', 'e', 'i', 'o', 'u'}

def vowels_count(s):
    """
    Count the number of vowels in a given word.

    Vowels in this case are 'a', 'e', 'i', 'o', 'u'. 'y' is also a vowel, 
    but only when it is at the end of the given word.

    Args:
        s (str): The input word.

    Returns:
        int: The number of vowels in the word.

    Example:
        >>> vowels_count("abcde")
        2
        >>> vowels_count("ACEDY")
        3
    """
    # Convert the string to lowercase for case-insensitive comparison
    s = s.lower()
    
    # Check if the word ends with 'y' and subtract 1 if it does
    if s.endswith('y'):
        return sum(1 for char in s[:-1] if char in VOWELS) + 1
    else:
        return sum(1 for char in s if char in VOWELS)

# Test the function
print(vowels_count("abcde"))  # Output: 2
print(vowels_count("ACEDY"))  # Output: 3
```
This script defines a function `vowels_count` that takes a string `s` as input and returns the number of vowels in the string. It uses a set `VOWELS` to store the vowels for efficient lookups. The function checks if the word ends with 'y' and adjusts the count accordingly. The script also includes test cases to demonstrate the function's behavior.