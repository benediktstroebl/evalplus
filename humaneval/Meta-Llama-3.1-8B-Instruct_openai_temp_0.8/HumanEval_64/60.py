```python
def vowels_count(s):
    """
    Counts the number of vowels in a given string.
    
    Vowels in this case are 'a', 'e', 'i', 'o', 'u'. 
    'Y' is also considered a vowel when it's at the end of the given word.
    
    Parameters:
    s (str): The input string.
    
    Returns:
    int: The number of vowels in the string.
    """
    # Convert the string to lower case to handle both lower and upper case letters
    s = s.lower()
    
    # Initialize a counter for vowels
    count = 0
    
    # Check if the word ends with 'y'
    is_y_at_end = s.endswith('y')
    
    # Iterate over each character in the string
    for char in s:
        # Check if the character is a vowel (excluding 'y' if it's not at the end)
        if (char in 'aeiou') or (char == 'y' and is_y_at_end):
            # Increment the vowel counter
            count += 1
    
    # Return the total count of vowels
    return count

# Test cases
print(vowels_count("abcde"))  # Expected output: 2
print(vowels_count("ACEDY"))  # Expected output: 3
print(vowels_count("aeiou"))  # Expected output: 5
print(vowels_count("y"))      # Expected output: 1
print(vowels_count("xy"))     # Expected output: 1 (for 'y' as it's at the end)
print(vowels_count(""))       # Expected output: 0
```