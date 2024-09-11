### Vowel Counter Script
```python
# Define a constant string with a fix for the problem statement
FIX = """
Add more test cases.
"""

def vowels_count(s):
    """
    Returns the number of vowels in the input string.
    
    Vowels in this case are 'a', 'e', 'i', 'o', 'u'. 
    'y' is also considered a vowel when it's at the end of the string.
    
    Parameters:
    s (str): The input string to count vowels from.
    
    Returns:
    int: The total count of vowels in the string.
    """
    # Initialize a counter for vowels
    count = 0
    
    # Check if the string is not empty
    if s:
        # Check if the last character is 'y' (for the special case)
        if len(s) > 1 and s[-1].lower() == 'y':
            # Count 'y' as a vowel if it's not the only character
            count += 1
        
        # Iterate over each character in the string
        for char in s:
            # Check if the character is a vowel (case-insensitive)
            if char.lower() in 'aeiou':
                # Increment the vowel count
                count += 1
    
    # Return the total vowel count
    return count

# Test the function with example inputs
print(vowels_count("abcde"))  # Output: 2
print(vowels_count("ACEDY"))  # Output: 3
```
This script defines a function `vowels_count` that takes a string input and returns the total count of vowels in the string. It handles the special case where 'y' is considered a vowel only when it's at the end of the string. The script includes a docstring to explain the function's behavior and includes example usage to demonstrate its functionality.