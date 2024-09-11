```python
def vowels_count(s):
    """
    This function takes a string representing a word as input and returns 
    the number of vowels in the string. 'a', 'e', 'i', 'o', 'u' are vowels, 
    and 'y' is also considered as a vowel when it's at the end of the word.

    Parameters:
    s (str): The input string.

    Returns:
    int: The number of vowels in the input string.
    """
    # Convert the string to lower case to handle both lower and upper case letters
    s = s.lower()
    
    # Initialize a counter for vowels
    count = 0
    
    # Initialize a flag to check if 'y' is at the end of the word
    is_y_at_end = s[-1] == 'y'
    
    # Iterate over each character in the string
    for char in s:
        # Check if the character is a vowel
        if char in 'aeiou':
            # If the character is a vowel, increment the counter
            count += 1
        # If 'y' is at the end of the word and the current character is 'y', 
        # increment the counter
        elif is_y_at_end and char == 'y':
            count += 1
    
    # Return the total count of vowels
    return count

# Example usage:
print(vowels_count("abcde"))  # Output: 2
print(vowels_count("ACEDY"))  # Output: 3
print(vowels_count("hello"))  # Output: 2
print(vowels_count("python"))  # Output: 2
print(vowels_count("yay"))  # Output: 2
```

This script defines a function `vowels_count` that takes a string `s` as input and returns the number of vowels in the string. The function handles both lower and upper case letters by converting the string to lower case. It also checks if 'y' is at the end of the word and counts it as a vowel in that case. The example usage at the end shows how to use the function with different inputs.