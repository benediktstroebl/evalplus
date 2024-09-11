```python
def vowels_count(s):
    """
    This function takes a string representing a word as input and returns the number of vowels in the string.
    Vowels in this case are 'a', 'e', 'i', 'o', 'u'. Here, 'y' is also a vowel, but only when it is at the end of the given word.

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
    # Convert the string to lowercase to simplify the vowel check
    s = s.lower()
    
    # Initialize a counter for the number of vowels
    count = 0
    
    # Check each character in the string
    for i, char in enumerate(s):
        # If the character is a vowel (or 'y' at the end of the string), increment the counter
        if char in 'aeiou' or (char == 'y' and i == len(s) - 1):
            count += 1
    
    # Return the total number of vowels
    return count

# Test cases
print(vowels_count("abcde"))  # Expected: 2
print(vowels_count("ACEDY"))  # Expected: 3
print(vowels_count("hello"))  # Expected: 2
print(vowels_count("aeiou"))  # Expected: 5
print(vowels_count("bcdfg"))  # Expected: 0
```

Note: The solution above uses a simple string check to identify vowels and the 'y' condition. It assumes that the input string is a single word (i.e., does not contain spaces). If you need to handle multi-word strings or other edge cases, additional logic may be required.