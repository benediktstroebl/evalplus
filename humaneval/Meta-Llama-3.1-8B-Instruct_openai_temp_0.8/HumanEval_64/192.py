```python
def vowels_count(s):
    """Write a function vowels_count which takes a string representing
    a word as input and returns the number of vowels in the string.
    Vowels in this case are 'a', 'e', 'i', 'o', 'u'. Here, 'y' is also a
    vowel, but only when it is at the end of the given word.

    Args:
        s (str): The input string.

    Returns:
        int: The number of vowels in the string.

    Example:
        >>> vowels_count("abcde")
        2
        >>> vowels_count("ACEDY")
        3
    """
    # Convert the string to lowercase to handle case-insensitive comparison
    s = s.lower()
    
    # Initialize a counter for vowels
    count = 0
    
    # Check if the last character is 'y'
    if s.endswith('y'):
        # If 'y' is at the end, count it as a vowel
        count += 1
        # Remove the 'y' from the string
        s = s[:-1]
    
    # Iterate over each character in the string
    for char in s:
        # Check if the character is a vowel
        if char in 'aeiou':
            # If the character is a vowel, increment the counter
            count += 1
    
    # Return the total count of vowels
    return count

# Test cases
print(vowels_count("abcde"))  # Output: 2
print(vowels_count("ACEDY"))  # Output: 3
print(vowels_count("Hello"))  # Output: 2
print(vowels_count("AEIOU"))  # Output: 5
print(vowels_count("bcdfg"))  # Output: 0
```

This script defines a function `vowels_count` that takes a string as input and returns the number of vowels in the string. The function is case-insensitive and considers 'y' as a vowel only if it is at the end of the string. The script also includes test cases to verify the correctness of the function.