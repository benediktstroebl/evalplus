```python
def vowels_count(s):
    """
    This function calculates the number of vowels in a given string.
    Vowels are 'a', 'e', 'i', 'o', 'u' and 'y' when at the end of the string.

    Parameters:
    s (str): The input string.

    Returns:
    int: The number of vowels in the string.
    """
    # Convert the string to lower case to handle both upper and lower case letters
    s = s.lower()
    
    # Initialize a counter for vowels
    count = 0
    
    # Check if the string is not empty
    if s:
        # Check if the last character is 'y'
        if s[-1] == 'y':
            # If the string ends with 'y', check if it does not end with 'ay' or 'ey' or 'iy' or 'oy' or 'uy'
            if s.endswith(("ay", "ey", "iy", "oy", "uy")):
                # If the string ends with 'y' and not a vowel, do not count 'y'
                pass
            else:
                # If the string ends with 'y', count 'y' as a vowel
                count += 1
        
        # Iterate over each character in the string
        for char in s:
            # Check if the character is a vowel
            if char in 'aeiou':
                # If the character is a vowel, increment the count
                count += 1
    
    # Return the count of vowels
    return count

# Test the function
print(vowels_count("abcde"))  # Expected output: 2
print(vowels_count("ACEDY"))  # Expected output: 3
print(vowels_count("aEy"))    # Expected output: 2
print(vowels_count("xY"))     # Expected output: 1
print(vowels_count(""))       # Expected output: 0
```

This script defines a function `vowels_count` that takes a string as input and returns the number of vowels in the string. The function first converts the string to lower case to handle both upper and lower case letters. It then checks if the string ends with 'y' and handles this case separately. Finally, it iterates over each character in the string and counts the vowels. If the string does not contain any vowels, the function returns 0.