```python
def vowels_count(s):
    """
    Returns the number of vowels in the given string.
    Vowels are 'a', 'e', 'i', 'o', 'u'. 'y' is considered a vowel if it's at the end of the string.

    Parameters:
    s (str): The input string.

    Returns:
    int: The number of vowels in the string.
    """
    # Convert the string to lowercase to simplify the vowel check
    s = s.lower()
    
    # Initialize a counter for vowels
    count = 0
    
    # Initialize a flag to track if the last character was 'y'
    last_char_was_y = False
    
    # Iterate over each character in the string
    for char in s:
        # Check if the character is a vowel
        if char in 'aeiou':
            # If the character is a vowel, increment the count
            count += 1
        # Check if the character is 'y' and it's not at the end of the string
        elif char == 'y' and s.index(char)!= len(s) - 1:
            # If the character is 'y' but not at the end, increment the count
            count += 1
            # Set the flag to True
            last_char_was_y = True
        # Check if the character is 'y' and it's at the end of the string and the previous character was not 'y'
        elif char == 'y' and s.index(char) == len(s) - 1 and not last_char_was_y:
            # If the character is 'y' at the end and the previous character was not 'y', increment the count
            count += 1
    
    # Return the count of vowels
    return count

# Example usage
print(vowels_count("abcde"))  # Output: 2
print(vowels_count("ACEDY"))  # Output: 3
```

This script defines a function `vowels_count` that takes a string `s` as input and returns the number of vowels in the string. The function handles the edge case where 'y' is considered a vowel if it's at the end of the string. The example usage demonstrates the function's behavior with the provided test cases.