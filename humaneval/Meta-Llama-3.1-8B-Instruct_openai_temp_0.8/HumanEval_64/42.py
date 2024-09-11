### Vowels Counting Function
```python
def vowels_count(s):
    """
    Returns the number of vowels in the given string.
    Vowels are 'a', 'e', 'i', 'o', 'u'. 'y' is a vowel if it is at the end.
    
    Parameters:
    s (str): The input string
    
    Returns:
    int: The number of vowels in the string
    """
    vowels = 'aeiou'
    count = 0
    # Check if the word ends with 'y'
    if s.lower().endswith('y'):
        # If it does, remove the 'y' and count it
        count += 1
        s = s[:-1]
    
    # Count the vowels
    for char in s.lower():
        if char in vowels:
            count += 1
    
    return count

# Example usage
print(vowels_count("abcde"))  # Output: 2
print(vowels_count("ACEDY"))  # Output: 3
```
This script defines the `vowels_count` function, which takes a string as input and returns the number of vowels in the string. It handles the special case where 'y' is a vowel if it is at the end of the string. The example usage demonstrates how to call the function with different inputs.