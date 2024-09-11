```python
def vowels_count(s):
    """
    This function counts the number of vowels in a given string.
    Vowels in this case are 'a', 'e', 'i', 'o', 'u'. 'Y' is considered a vowel
    only when it is at the end of the given word.

    Args:
        s (str): The input string.

    Returns:
        int: The number of vowels in the string.

    """
    # Convert the string to lowercase for simplicity
    s = s.lower()
    
    # Initialize a counter for vowels
    count = 0
    
    # Check if the last character is 'y'
    if s[-1] == 'y':
        # If 'y' is at the end, increment the count
        s = s[:-1]
        count += 1
    
    # Iterate over the characters in the string
    for char in s:
        # Check if the character is a vowel
        if char in 'aeiou':
            # If it's a vowel, increment the count
            count += 1
    
    # Return the total count of vowels
    return count

# Test the function
print(vowels_count("abcde"))  # Expected output: 2
print(vowels_count("ACEDY"))  # Expected output: 3
```

This script defines a function `vowels_count` that takes a string as input and returns the count of vowels in the string. It considers 'y' as a vowel only when it's at the end of the string. The function uses a simple loop to iterate over the characters in the string, checking each one to see if it's a vowel. If it is, the function increments the count. Finally, the function returns the total count of vowels.