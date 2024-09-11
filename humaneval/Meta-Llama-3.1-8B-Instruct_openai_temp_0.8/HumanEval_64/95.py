```python
def vowels_count(s):
    """
    This function takes a string representing a word as input and returns 
    the number of vowels in the string. Vowels in this case are 'a', 'e', 'i', 
    'o', 'u'. Here, 'y' is also a vowel, but only when it is at the end of 
    the given word.

    Parameters:
    s (str): The input string.

    Returns:
    int: The number of vowels in the string.

    Examples:
    >>> vowels_count("abcde")
    2
    >>> vowels_count("ACEDY")
    3
    """
    
    # Convert the string to lowercase to simplify the vowel check
    s = s.lower()
    
    # Initialize a counter for the number of vowels
    count = 0
    
    # Iterate over each character in the string
    for i, char in enumerate(s):
        # If the character is a vowel or 'y' at the end of the string, increment the counter
        if char in 'aeiou' or ((char == 'y') and (i == len(s) - 1)):
            count += 1
    
    # Return the total count of vowels
    return count

# Test cases
print(vowels_count("abcde"))  # Expected output: 2
print(vowels_count("ACEDY"))  # Expected output: 3
```

This script defines a function `vowels_count` that takes a string `s` as input and returns the number of vowels in `s`, considering 'y' as a vowel only if it is at the end of the string. The script also includes test cases to demonstrate the function's behavior.