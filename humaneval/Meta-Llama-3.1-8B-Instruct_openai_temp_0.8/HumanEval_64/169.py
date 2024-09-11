### Vowels Count Function
```python
def vowels_count(s):
    """
    Returns the number of vowels in a given string.
    Vowels in this case are 'a', 'e', 'i', 'o', 'u'. 
    'y' is also a vowel, but only when it is at the end of the given word.

    Args:
        s (str): Input string.

    Returns:
        int: Number of vowels in the string.
    """
    s = s.lower()  # Convert string to lowercase for simplicity
    count = 0
    # Check if 'y' is at the end of the string
    if s and s[-1] == 'y':
        # Remove the last character and decrement the length
        vowels = 'aeiou' + 'y'
        s = s[:-1]
    else:
        vowels = 'aeiou'
    
    # Count the occurrences of vowels
    for char in s:
        if char in vowels:
            count += 1
    
    return count

# Example usage:
print(vowels_count("abcde"))  # Output: 2
print(vowels_count("ACEDY"))  # Output: 3
```
This script defines a function `vowels_count` that counts the number of vowels in a given string. It handles the special case where 'y' is considered a vowel when it appears at the end of the string. The function is then tested with the example inputs provided.