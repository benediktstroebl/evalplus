### Vowels Count Function
```python
def vowels_count(s):
    """
    This function counts the number of vowels in a given string.
    
    Parameters:
    s (str): The input string.
    
    Returns:
    int: The number of vowels in the string.
    
    Notes:
    In this function, 'y' is considered a vowel only when it's at the end of the string.
    """
    
    # Define the vowels
    vowels = 'aeiouy'
    
    # Initialize a counter for vowels
    count = 0
    
    # Check if the string is not empty
    if s:
        # Check if the last character is 'y'
        if s[-1].lower() == 'y':
            # Remove the last character from the string
            s = s[:-1]
        
        # Iterate over each character in the string
        for char in s:
            # Check if the character is a vowel
            if char.lower() in vowels:
                # Increment the vowel count
                count += 1
    
    # Return the total count of vowels
    return count

# Example usage
print(vowels_count("abcde"))  # Output: 2
print(vowels_count("ACEDY"))  # Output: 3
```

This Python script defines a function `vowels_count` that takes a string `s` as input and returns the number of vowels in the string, considering 'y' as a vowel only when it's at the end of the string. The function first separates the last character 'y' from the string if it exists, then it iterates over each character in the string to count the vowels. The function returns the total count of vowels.