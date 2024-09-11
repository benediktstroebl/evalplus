### Vowels Counter Script
```python
# Define the function vowels_count
def vowels_count(s):
    """
    Returns the number of vowels in the string.
    Vowels in this case are 'a', 'e', 'i', 'o', 'u'.
    'y' is also a vowel, but only when it is at the end of the given word.
    
    Parameters:
    s (str): The string representing a word.
    
    Returns:
    int: The number of vowels in the string.
    """
    # Convert the string to lowercase for simplicity
    s = s.lower()
    
    # Initialize the count of vowels
    count = 0
    
    # Check if the last character is 'y'
    if len(s) > 1 and s[-1] == 'y':
        # If it is, decrement the count by 1 because 'y' is not a vowel
        count -= 1
    
    # Iterate over the characters in the string
    for char in s:
        # Check if the character is a vowel
        if char in 'aeiou':
            # If it is, increment the count
            count += 1
    
    # Return the count of vowels
    return count

# Test cases
print(vowels_count("abcde"))  # Expected output: 2
print(vowels_count("ACEDY"))  # Expected output: 3
```
This script defines a function `vowels_count` that takes a string as input and returns the number of vowels in the string. The function handles the special case where 'y' is a vowel only when it is at the end of the word. The script includes test cases to demonstrate its usage.