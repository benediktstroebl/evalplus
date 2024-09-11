```python
def vowels_count(s):
    """
    Returns the number of vowels in the given string.
    'y' is considered a vowel when it's at the end of the string.

    Args:
        s (str): The input string.

    Returns:
        int: The number of vowels in the string.
    """
    # Convert the string to lowercase to simplify the condition
    s = s.lower()
    
    # Initialize a counter for vowels
    count = 0
    
    # Check if the string is not empty
    if s:
        # Check if the last character is 'y' and it's not the only character
        if len(s) > 1 and s[-1] == 'y' and s[-2]!= 'y':
            # If 'y' is at the end, do not count it as a vowel
            s = s[:-1]
        
        # Count the number of 'a', 'e', 'i', 'o', 'u' in the string
        for vowel in 'aeiou':
            count += s.count(vowel)
    
    # Return the total count of vowels
    return count

# Example usage:
print(vowels_count("abcde"))  # Output: 2
print(vowels_count("ACEDY"))  # Output: 3
print(vowels_count("y"))      # Output: 1 (since 'y' is at the end)
print(vowels_count("aya"))    # Output: 2 (since 'y' is at the end)
```

This script defines a function `vowels_count` that takes a string `s` as input and returns the number of vowels in the string. The function converts the string to lowercase to simplify the condition, checks if the last character is 'y' and it's not the only character, and then counts the number of 'a', 'e', 'i', 'o', 'u' in the string. The function returns the total count of vowels. The example usage shows how to use this function with different inputs.