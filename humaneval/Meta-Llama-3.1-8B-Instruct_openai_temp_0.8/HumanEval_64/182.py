### Vowels Count Function
```python
def vowels_count(s):
    """
    Counts the number of vowels in a given string.

    Vowels are 'a', 'e', 'i', 'o', 'u'. 'y' is also considered a vowel if it's at the end of the word.

    Args:
        s (str): The input string.

    Returns:
        int: The number of vowels in the string.
    """
    # Convert the string to lower case for simplicity
    s = s.lower()
    
    # Initialize count to 0
    count = 0
    
    # Check if the string is not empty
    if s:
        # Check if the last character is 'y'
        if s[-1] == 'y':
            # If it's 'y', check if it's at the end of the word
            if s.count('y') == 1:
                # If it's at the end, increment the count
                count += 1
        
        # Count the vowels
        for char in s:
            # Check if the character is a vowel
            if char in 'aeiou':
                # If it's a vowel, increment the count
                count += 1
    
    # Return the count
    return count

# Test cases
print(vowels_count("abcde"))  # Output: 2
print(vowels_count("ACEDY"))  # Output: 3
print(vowels_count("hello"))  # Output: 2
print(vowels_count("y"))  # Output: 1
```

This script defines a function `vowels_count` that takes a string as input and returns the number of vowels in the string. It considers 'y' as a vowel if it's at the end of the word. The test cases are included to demonstrate the function's functionality.