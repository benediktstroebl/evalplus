```python
def vowels_count(s):
    """
    Returns the number of vowels in the given string. 'Y' is considered a vowel only when it's at the end of the string.
    
    Parameters:
    s (str): The input string.
    
    Returns:
    int: The number of vowels in the string.
    """
    
    # Initialize a counter for vowels
    count = 0
    
    # Check if the last character is 'y' (considered vowel at the end)
    last_char_is_y = s[-1].lower() == 'y'
    
    # Iterate over each character in the string
    for char in s:
        # If the character is a vowel (lowercase) and not at the end and it's not counted last_char_is_y, increment the count
        if char.lower() in 'aeiou' and char.lower()!= 'y' and not last_char_is_y:
            count += 1
        # If the character is 'Y' (at the end), increment the count
        elif char.lower() == 'y' and last_char_is_y:
            count += 1
    
    # Return the count of vowels
    return count


# Test cases
print(vowels_count("abcde"))  # Expected output: 2
print(vowels_count("ACEDY"))  # Expected output: 3
print(vowels_count("hello world"))  # Expected output: 3
print(vowels_count("aeiou"))  # Expected output: 5
print(vowels_count("y"))  # Expected output: 1
```
This script defines a function `vowels_count` that takes a string as input and returns the number of vowels in the string. The function considers 'y' as a vowel only when it's at the end of the string. The test cases at the end demonstrate the function's usage.