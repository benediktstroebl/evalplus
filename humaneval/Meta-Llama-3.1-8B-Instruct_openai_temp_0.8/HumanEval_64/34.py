```python
def vowels_count(s):
    """
    This function counts the number of vowels in a given string.
    Vowels are 'a', 'e', 'i', 'o', 'u'. 'y' is considered a vowel only if it's at the end of the word.

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
    
    # Initialize a counter for vowels
    vowel_count = 0
    
    # Initialize a flag to check if 'y' is at the end of the string
    y_at_end = s[-1] == 'y' if len(s) > 1 else False
    
    # Iterate over each character in the string
    for char in s:
        # Check if the character is a vowel
        if char in 'aeiou':
            # If it's a vowel, increment the counter
            vowel_count += 1
        elif char == 'y' and y_at_end:
            # If it's 'y' and it's at the end of the string, increment the counter
            vowel_count += 1
    
    # Return the total vowel count
    return vowel_count

# Test cases
print(vowels_count("abcde"))  # Expected output: 2
print(vowels_count("ACEDY"))  # Expected output: 3
print(vowels_count("hello"))  # Expected output: 2
print(vowels_count("AEIOUY"))  # Expected output: 5
print(vowels_count("bcd"))  # Expected output: 0
```

This script defines a function `vowels_count` that takes a string `s` as input and returns the number of vowels in the string. It also includes example test cases to demonstrate the function's behavior. The function uses a simple loop to iterate over each character in the string, checks if the character is a vowel, and increments a counter accordingly. It also handles the special case of 'y' at the end of the string.