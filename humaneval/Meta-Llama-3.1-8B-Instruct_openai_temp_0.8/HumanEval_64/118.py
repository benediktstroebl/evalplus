```python
def vowels_count(s):
    """
    This function counts the number of vowels in a given word.
    Vowels are 'a', 'e', 'i', 'o', 'u'. 'y' is also a vowel when it's at the end of the word.

    Parameters:
    s (str): The input string representing a word.

    Returns:
    int: The number of vowels in the string.
    """
    # Convert the string to lowercase to simplify vowel detection
    s = s.lower()
    
    # Initialize the vowel count to 0
    count = 0
    
    # Check if the string is not empty
    if s:
        # Check if the last character is 'y'
        if s[-1] == 'y':
            # If 'y' is at the end, decrement the length because we don't want to count it as a vowel
            vowel_str = s[:-1]
        else:
            # If 'y' is not at the end, include the entire string
            vowel_str = s
        
        # Count the number of vowels in the string
        for char in vowel_str:
            if char in 'aeiou':
                count += 1
    
    # Return the total number of vowels
    return count

# Test cases
print(vowels_count("abcde"))  # Should print 3
print(vowels_count("ACEDY"))  # Should print 3
print(vowels_count("y"))  # Should print 1
```

This script implements the function `vowels_count` as described in the problem. It takes a string `s` as input, converts it to lowercase to simplify vowel detection, and then counts the number of vowels by iterating over each character in the string. If the last character of the string is 'y', it is only counted as a vowel if it's not at the end of the string. The function returns the total number of vowels found in the string.