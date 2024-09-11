```python
def vowels_count(s):
    """
    This function counts the number of vowels in a given string.
    'Y' is considered a vowel if it is at the end of the string.
    
    Parameters:
    s (str): The input string.
    
    Returns:
    int: The number of vowels in the string.
    """
    # Initialize count of vowels
    count = 0
    
    # Special case for 'Y' at the end of the string
    if s.lower().endswith('y'):
        count += 1
    
    # Iterate over each character in the string
    for char in s.lower():
        # Check if the character is a vowel
        if char in 'aeiou':
            # If it is, increment the count
            count += 1
    
    # Return the total count of vowels
    return count

# Test cases
input_words = ["abcde", "ACEDY", "hello", "AEIOU", "y"]
for word in input_words:
    print(f"Number of vowels in '{word}': {vowels_count(word)}")
```

This script defines a function `vowels_count` that counts the number of vowels in a given string. The function handles the special case where 'Y' is at the end of the string and iterates over each character in the string to count the vowels. The test cases at the end demonstrate the function's usage with different input strings.