### Vowels Count Function
```python
def vowels_count(s):
    """
    Returns the number of vowels in the given string.

    Vowels are 'a', 'e', 'i', 'o', 'u'. 'y' is considered a vowel if it's at the end of the word.

    Args:
        s (str): The input string.

    Returns:
        int: The number of vowels in the string.
    """
    # Convert the string to lowercase for simplicity
    s = s.lower()
    
    # Initialize a counter for vowels
    count = 0
    
    # Check if the last character is 'y'
    if s[-1] == 'y':
        # If it is, check for vowels in the rest of the string
        rest_of_string = s[:-1]
        count = sum(1 for char in rest_of_string if char in 'aeiou')
        # Add 1 to the count because 'y' is a vowel
        count += 1
    else:
        # If it's not 'y', check for all vowels
        count = sum(1 for char in s if char in 'aeiou')
    
    return count

# Test cases
print(vowels_count("abcde"))  # Expected output: 2
print(vowels_count("ACEDY"))  # Expected output: 3
print(vowels_count("hello"))  # Expected output: 2
print(vowels_count("worldy"))  # Expected output: 2
```

This script defines a function `vowels_count` that counts the number of vowels in a given string. It handles the special case where 'y' is considered a vowel if it's at the end of the word. The script includes test cases to demonstrate its usage.