```python
def vowels_count(s):
    """
    This function takes a string representing a word as input and returns
    the number of vowels in the string. Vowels in this case are 'a', 'e', 'i', 
    'o', 'u'. Here, 'y' is also a vowel, but only when it is at the end of the 
    given word.

    Parameters:
    s (str): The input string.

    Returns:
    int: The number of vowels in the string.
    """
    # Convert the string to lowercase for simplicity
    s = s.lower()
    
    # Initialize a counter for vowels
    count = 0
    
    # Initialize a flag to check if the word ends with 'y'
    is_last_char_y = False
    
    # Check if the word is not empty
    if s:
        # Check if the word ends with 'y'
        if s[-1] == 'y':
            is_last_char_y = True
            # Remove the last character 'y' from the word
            s = s[:-1]
    
    # Iterate over the string
    for char in s:
        # Check if the character is a vowel
        if char in 'aeiou':
            # If the character is a vowel, increment the counter
            count += 1
    
    # If the word ends with 'y', increment the counter by 1
    if is_last_char_y:
        count += 1
    
    # Return the count of vowels
    return count

# Test cases
print(vowels_count("abcde"))  # Output: 2
print(vowels_count("ACEDY"))  # Output: 3
```