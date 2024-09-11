```python
# Define the function vowels_count that takes a string s as input
def vowels_count(s):
    """
    Returns the number of vowels in the given string.
    
    Vowels are 'a', 'e', 'i', 'o', 'u'. 'y' is considered a vowel only if it's at the end of the word.
    
    Parameters:
    s (str): The input string.
    
    Returns:
    int: The number of vowels in the string.
    """
    # Initialize count of vowels to 0
    count = 0
    
    # Convert the string to lowercase for simplicity
    s = s.lower()
    
    # Iterate over each character in the string
    for i, char in enumerate(s):
        # If the character is a vowel and it's not at the end of the string, increment count
        if char in 'aeiou' and i < len(s) - 1:
            count += 1
        # If the character is 'y' and it's at the end of the string, increment count
        elif char == 'y' and i == len(s) - 1:
            count += 1
        # If the character is a lowercase vowel, increment count
        elif char in 'aeiou':
            count += 1
    
    # Return the count of vowels
    return count

# Example usage:
print(vowels_count("abcde"))  # Output: 2
print(vowels_count("ACEDY"))  # Output: 3
```

This script defines the function `vowels_count` that takes a string `s` as input and returns the number of vowels in the string. The function considers 'y' as a vowel only if it's at the end of the word. The script also includes example usage of the function.