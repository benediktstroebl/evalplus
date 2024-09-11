### Vowels Count Function
```python
# Define a string of vowels with 'y' considered only when at the end
VOWELS = {'a', 'e', 'i', 'o', 'u'}

def vowels_count(s):
    """
    Returns the number of vowels in a given string.

    Vowels are 'a', 'e', 'i', 'o', 'u'. 'y' is considered a vowel only when it's at the end of the word.

    Args:
        s (str): Input string representing a word.

    Returns:
        int: The number of vowels in the string.
    """
    # Convert the string to lowercase for case-insensitive comparison
    s = s.lower()
    
    # Initialize a counter for vowels
    count = 0
    
    # Check if the last character is 'y' (considered a vowel only when at the end)
    if s and s[-1] == 'y':
        # If the last character is 'y', subtract 1 from the length because we'll add it separately
        word_len = len(s) - 1
    else:
        # If not, consider the whole word
        word_len = len(s)
    
    # Count vowels
    for i in range(word_len):
        if s[i] in VOWELS:
            count += 1
    
    # If the last character is 'y', add it to the count
    if s and s[-1] == 'y':
        count += 1
    
    return count

# Example usage:
print(vowels_count("abcde"))  # Output: 2
print(vowels_count("ACEDY"))  # Output: 3
```
This script defines a function `vowels_count` that meets the given requirements. It takes a string as input, counts the vowels (considering 'y' only when at the end), and returns the count. The function is well-documented with a docstring explaining its purpose, arguments, and return value. The script includes example usage to demonstrate its functionality.