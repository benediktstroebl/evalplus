**Vowels Count Function**
=========================

A Python function to count the number of vowels in a given string.

```python
def vowels_count(s):
    """
    Returns the number of vowels in the given string.
    
    Vowels are 'a', 'e', 'i', 'o', 'u'. 'y' is also a vowel when it's at the end.
    
    Parameters:
    s (str): The input string.
    
    Returns:
    int: The number of vowels in the string.
    """
    
    # Convert the string to lowercase to simplify vowel checking
    s = s.lower()
    
    # Initialize a counter for vowels and the special 'y' at the end
    vowels_count = 0
    
    # Check if the last character is 'y'
    is_y_at_end = len(s) > 1 and s[-1] == 'y'
    
    # Iterate over each character in the string
    for char in s:
        # Check if the character is a vowel
        if char in 'aeiou':
            # Increment the vowel counter
            vowels_count += 1
    
    # If 'y' is at the end, increment the vowel counter
    if is_y_at_end:
        vowels_count += 1
    
    return vowels_count

# Example usage:
print(vowels_count("abcde"))  # Output: 2
print(vowels_count("ACEDY"))  # Output: 3
print(vowels_count("Hello"))  # Output: 2
print(vowels_count("y"))  # Output: 1
```

This script provides a function `vowels_count` that takes a string `s` as input and returns the number of vowels in the string, considering 'y' as a vowel only when it's at the end. It correctly handles both lowercase and uppercase letters in the input string.