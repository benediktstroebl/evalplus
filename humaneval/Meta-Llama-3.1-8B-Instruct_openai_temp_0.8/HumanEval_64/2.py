```python
def vowels_count(s):
    """
    Counts the number of vowels in a given word.

    A vowel is defined as 'a', 'e', 'i', 'o', 'u'. 'y' is also considered a
    vowel if it is at the end of the word.

    Args:
        s (str): The input word.

    Returns:
        int: The count of vowels in the word.

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
    
    # Iterate over each character in the string
    for i, char in enumerate(s):
        # Check if the character is a vowel or 'y' at the end of the string
        if char in 'aeiou' or (char == 'y' and i == len(s) - 1):
            # If it is, increment the vowel count
            count += 1
    
    # Return the total count of vowels
    return count

# Test cases
print(vowels_count("abcde"))  # Expected output: 2
print(vowels_count("ACEDY"))  # Expected output: 3
print(vowels_count("AEIOU"))  # Expected output: 5
print(vowels_count("bcdfg"))  # Expected output: 0
print(vowels_count("y"))      # Expected output: 1
print(vowels_count(""))       # Expected output: 0
```

In this script, the `vowels_count` function takes a string as input, converts it to lowercase to handle case-insensitive comparison, and then iterates over each character in the string. If the character is a vowel ('a', 'e', 'i', 'o', 'u') or 'y' at the end of the string, it increments the vowel count. Finally, it returns the total count of vowels. The test cases at the end of the script demonstrate the function's behavior with different inputs.