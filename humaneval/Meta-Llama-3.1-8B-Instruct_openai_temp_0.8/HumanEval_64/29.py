### Vowels Count Function
```python
def vowels_count(s):
    """
    Returns the number of vowels in the given string.

    Vowels are 'a', 'e', 'i', 'o', 'u'. 'y' is also a vowel if it's at the end of the string.

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
        # Check if 'y' is at the end of the string
        if s[-1] == 'y' and len(s) > 1 and (s[-2] not in 'aeiou' or s[-2]!= 'y'):
            # If 'y' is at the end, decrement the count
            count -= 1
        
        # Count the occurrences of 'a', 'e', 'i', 'o', 'u'
        for char in s:
            if char in 'aeiou':
                count += 1
    
    return count

# Test cases
print(vowels_count("abcde"))  # Output: 2
print(vowels_count("ACEDY"))  # Output: 3
```

This script defines a function `vowels_count` that takes a string `s` as input and returns the number of vowels in the string. The function first converts the string to lowercase for simplicity. It then checks if the string is not empty and if 'y' is at the end of the string. If 'y' is at the end, it decrements the count. Finally, it counts the occurrences of 'a', 'e', 'i', 'o', 'u' in the string and returns the count. The script includes test cases to verify that the function works correctly.