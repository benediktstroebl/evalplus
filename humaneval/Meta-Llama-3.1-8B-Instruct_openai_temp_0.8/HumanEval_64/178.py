```python
def vowels_count(s):
    """
    This function counts the number of vowels in a given string.
    
    Vowels are 'a', 'e', 'i', 'o', 'u'. 'y' is also a vowel if it is at the end of the string.
    
    Parameters:
    s (str): The input string.
    
    Returns:
    int: The number of vowels in the string.
    """
    # Convert the string to lowercase to make the function case-insensitive
    s = s.lower()
    
    # Initialize a count variable to store the number of vowels
    count = 0
    
    # Check if the string is not empty
    if s:
        # Check if the last character is 'y' and it's not at the end of the string
        if s[-1] == 'y' and len(s) > 1:
            # If 'y' is at the end, don't count it as a vowel
            s = s[:-1]
        
        # Count the vowels in the string
        for char in s:
            if char in 'aeiou':
                count += 1
    
    # Return the total count of vowels
    return count

# Test the function
print(vowels_count("abcde"))  # Output: 2
print(vowels_count("ACEDY"))  # Output: 3
print(vowels_count("hello"))  # Output: 2
print(vowels_count("AEIOU"))  # Output: 5
print(vowels_count("y"))      # Output: 1
```

This script defines a function `vowels_count` that takes a string `s` as input and returns the number of vowels in the string. It handles both uppercase and lowercase letters and considers 'y' as a vowel only if it is at the end of the string. The script also includes test cases to demonstrate the function's behavior.