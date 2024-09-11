### Vowels Count Function
```python
def vowels_count(s):
    """
    This function takes a string representing a word as input and returns 
    the number of vowels in the string. Vowels in this case are 'a', 'e', 
    'i', 'o', 'u'. 'Y' is also a vowel, but only when it is at the end of 
    the given word.

    Args:
        s (str): The input string.

    Returns:
        int: The number of vowels in the string.
    """
    # Convert the string to lower case to make the function case-insensitive
    s = s.lower()
    
    # Initialize a counter for vowels
    count = 0
    
    # Iterate over each character in the string
    for char in s:
        # Check if the character is a vowel or 'y' at the end of the string
        if char in 'aeiou' or (char == 'y' and s.endswith('y')):
            # Increment the vowel counter
            count += 1
    
    # Return the total count of vowels
    return count

# Example usage
print(vowels_count("abcde"))  # Output: 2
print(vowels_count("ACEDY"))  # Output: 3
print(vowels_count("hello"))  # Output: 2
```
This script defines a function `vowels_count` that counts the number of vowels in a given string. It converts the input string to lower case to make the function case-insensitive, then iterates over each character in the string. If a character is a vowel (or 'y' at the end of the string), it increments a vowel counter. Finally, it returns the total count of vowels.