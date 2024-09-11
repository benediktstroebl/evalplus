### Vowels Count Function
```python
def vowels_count(s):
    """
    Counts the number of vowels in a given string. 
    Vowels are 'a', 'e', 'i', 'o', 'u'. 
    'y' is also a vowel when it's at the end of the word.
    
    Parameters:
    s (str): The input string.

    Returns:
    int: The number of vowels in the string.
    """
    # Convert the string to lowercase for simplicity
    s = s.lower()
    
    # Initialize a counter for vowels
    count = 0
    
    # Check if the string is not empty
    if s:
        # Check if the last character is 'y'
        if s[-1] == 'y':
            # If 'y' is at the end, count it as a vowel
            count += 1
        # Check for vowels in the string
        for char in s:
            if char in 'aeiou':
                # If the character is a vowel, increment the counter
                count += 1
    
    # Return the total count of vowels
    return count

# Example usage:
print(vowels_count("abcde"))  # Output: 2
print(vowels_count("ACEDY"))  # Output: 3
```
This script defines a function `vowels_count` that takes a string as input and returns the count of vowels in the string. It handles the special case where 'y' is a vowel when it's at the end of the word. The function uses a simple loop to iterate over the characters in the string and checks for vowels. The example usage demonstrates the function's behavior with different inputs.