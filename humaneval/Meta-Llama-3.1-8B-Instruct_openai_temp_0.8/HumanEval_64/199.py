```python
def vowels_count(s):
    """
    Returns the number of vowels in the given string.
    Vowels are 'a', 'e', 'i', 'o', 'u'. 'y' is a vowel when it is at the end of the word.
    
    Parameters:
    s (str): The input string.
    
    Returns:
    int: The number of vowels in the string.
    """
    # Convert the string to lower case to handle both lower and upper case letters
    s = s.lower()
    
    # Initialize the vowel count to 0
    count = 0
    
    # Check if the string is not empty
    if s:
        # Check if the last character is 'y'
        if s[-1] == 'y':
            # If 'y' is at the end, increment the count by 1
            count += 1
        
        # Iterate over each character in the string
        for char in s:
            # Check if the character is a vowel
            if char in 'aeiou':
                # If the character is a vowel, increment the count by 1
                count += 1
    
    # Return the vowel count
    return count

# Test cases
print(vowels_count("abcde"))  # Output: 2
print(vowels_count("ACEDY"))  # Output: 3
print(vowels_count("a"))      # Output: 1
print(vowels_count("y"))      # Output: 1
print(vowels_count(""))       # Output: 0
```

This script defines a function `vowels_count` that takes a string `s` as input and returns the number of vowels in `s`. The function handles both lower and upper case letters by converting the string to lower case. It also counts 'y' as a vowel only when it is at the end of the string. The script includes several test cases to demonstrate the function's correctness.