```python
def vowels_count(s):
    """
    This function counts the number of vowels in a given string.
    Vowels are 'a', 'e', 'i', 'o', 'u'. 'y' is also considered a vowel if it's at the end of the string.
    
    Parameters:
    s (str): The input string.
    
    Returns:
    int: The number of vowels in the string.
    """
    
    # Convert the string to lowercase for simplicity
    s = s.lower()
    
    # Initialize a counter for vowels
    count = 0
    
    # Check if the last character is 'y' (in this case, it's a vowel)
    if s and s[-1] == 'y':
        # If it is, remove it and add 1 to the count
        s = s[:-1]
        count += 1
    
    # Iterate over each character in the string
    for char in s:
        # Check if the character is a vowel
        if char in 'aeiou':
            # If it is, increment the count
            count += 1
    
    # Return the total count
    return count

# Test the function
print(vowels_count("abcde"))  # Expected output: 2
print(vowels_count("ACEDY"))  # Expected output: 3
```

This code defines a function `vowels_count` that counts the number of vowels in a given string. It first checks if the last character is 'y' and removes it if it is, since 'y' is considered a vowel only when it's at the end of the string. Then it iterates over each character in the string and increments the count if the character is a vowel. Finally, it returns the total count.