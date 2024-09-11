### Vowels Count Function
```python
def vowels_count(s):
    """
    This function calculates the number of vowels in a given string.
    Vowels in this case are 'a', 'e', 'i', 'o', 'u'. 
    'y' is also a vowel, but only when it is at the end of the given word.

    Args:
        s (str): The input string.

    Returns:
        int: The number of vowels in the string.
    """
    # Convert the string to lowercase for simplicity
    s = s.lower()
    
    # Initialize count of vowels
    count = 0
    
    # Check if the last character is 'y'
    is_last_char_y = s and s[-1] == 'y'
    
    # Iterate over the characters in the string
    for char in s:
        # Check if the character is a vowel or 'y' at the end of the word
        if char in 'aeiou' or (is_last_char_y and char == 'y'):
            # Increment the vowel count
            count += 1
    
    # Return the total count of vowels
    return count

# Example usage:
print(vowels_count("abcde"))  # Output: 2
print(vowels_count("ACEDY"))  # Output: 3
```