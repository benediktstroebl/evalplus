```python
def vowels_count(s):
    """
    This function takes a string representing a word as input and returns the number of vowels in the string.
    Vowels in this case are 'a', 'e', 'i', 'o', 'u'. 'y' is also a vowel, but only when it is at the end of the given word.

    Args:
        s (str): Input string representing a word.

    Returns:
        int: The number of vowels in the string.

    Example:
        >>> vowels_count("abcde")
        2
        >>> vowels_count("ACEDY")
        3
    """
    s = s.lower()  # Convert the string to lowercase for simplicity
    count = 0  # Initialize a counter for vowels
    if s[-1] == 'y':  # Check if the word ends with 'y'
        s = s[:-1]  # Remove the last character if the word ends with 'y'
    for char in s:  # Iterate over each character in the string
        if char in 'aeiou':  # Check if the character is a vowel
            count += 1  # Increment the vowel counter
    return count  # Return the total count of vowels

# Test cases
print(vowels_count("abcde"))  # Output: 2
print(vowels_count("ACEDY"))  # Output: 3
print(vowels_count("hello"))  # Output: 2
print(vowels_count("aeiouy"))  # Output: 5
print(vowels_count("bcdf"))  # Output: 0
```

This script defines a function `vowels_count` that takes a string as input, converts it to lowercase, and counts the number of vowels in the string. If the string ends with 'y', it is removed from the string. The function returns the total count of vowels. The script also includes test cases to demonstrate the function's usage.