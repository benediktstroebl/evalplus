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
    # Remove the last character if it is 'y' to handle the special case
    if s and s[-1].lower() == 'y':
        s = s[:-1]
    
    # Convert the string to lowercase for simplicity
    s = s.lower()
    
    # Initialize a counter for the number of vowels found
    count = 0
    
    # Iterate over the characters in the string
    for char in s:
        # Check if the character is a vowel
        if char in 'aeiou':
            # Increment the vowel count
            count += 1
    
    # Return the total number of vowels found
    return count

# Test cases
print(vowels_count("abcde"))  # Expected output: 2
print(vowels_count("ACEDY"))  # Expected output: 3
print(vowels_count("hello"))  # Expected output: 2
print(vowels_count("World"))  # Expected output: 1
```

This script defines a function `vowels_count` that counts the number of vowels in a given string, with the special case handling of 'y' at the end of the string. The function iterates over the characters in the string, checking each one to see if it's a vowel. If it is, the function increments a counter. At the end, the function returns the total number of vowels found. The test cases at the end demonstrate the function's behavior with different inputs.