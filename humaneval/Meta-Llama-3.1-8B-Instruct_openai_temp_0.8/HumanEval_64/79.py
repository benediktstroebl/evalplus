### Vowels Count Function
```python
def vowels_count(s):
    """
    Returns the number of vowels in the given string.
    
    Vowels are 'a', 'e', 'i', 'o', 'u'. 'y' is also a vowel when it's at the end of the word.
    
    Parameters:
    s (str): The input string.
    
    Returns:
    int: The number of vowels in the string.
    """
    
    # Convert the string to lowercase to simplify vowel detection
    s = s.lower()
    
    # Initialize the vowel count
    count = 0
    
    # Check each character in the string
    for i, char in enumerate(s):
        # If the character is a vowel (or 'y' at the end of the string)
        if char in 'aeiou' or (char == 'y' and i == len(s) - 1):
            # Increment the vowel count
            count += 1
    
    # Return the total vowel count
    return count

# Example usage:
print(vowels_count("abcde"))  # Output: 2
print(vowels_count("ACEDY"))  # Output: 3
```

This function converts the input string to lowercase to simplify vowel detection, then checks each character in the string. If the character is a vowel (or 'y' at the end of the string), it increments the vowel count. Finally, it returns the total vowel count.