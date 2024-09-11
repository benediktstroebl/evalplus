```python
# Define a function vowels_count that takes a string s as input
def vowels_count(s):
    """
    This function returns the count of vowels in a given string.
    Vowels are 'a', 'e', 'i', 'o', 'u'. 'y' is also considered a vowel when it's at the end of the string.

    Parameters:
    s (str): The input string.

    Returns:
    int: The count of vowels in the string.
    """
    # Define the vowels as a set for efficient lookups
    vowels = {'a', 'e', 'i', 'o', 'u'}
    
    # Check if the string is empty
    if not s:
        return 0
    
    # Check if the last character is 'y'
    if s[-1].lower() == 'y':
        # Remove the last character and consider 'y' as a vowel
        vowels.add('y')
        
    # Initialize the vowel count
    count = 0
    
    # Iterate over the characters in the string
    for char in s:
        # Check if the character is a vowel
        if char.lower() in vowels:
            # Increment the vowel count
            count += 1
    
    # Return the vowel count
    return count

# Test the function
print(vowels_count("abcde"))  # Expected output: 2
print(vowels_count("ACEDY"))  # Expected output: 3
```

This script defines a function `vowels_count` that counts the number of vowels in a given string. It considers 'y' as a vowel when it's at the end of the string. The function uses a set to store the vowels for efficient lookups. The script also includes test cases to demonstrate the function's correctness.