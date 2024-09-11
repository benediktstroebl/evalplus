```python
def vowels_count(s):
    """
    This function calculates the number of vowels in a given word.
    Vowels in this case are 'a', 'e', 'i', 'o', 'u'. The letter 'y' is also a vowel, 
    but only when it is at the end of the given word.

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
    # Convert the string to lowercase to handle case insensitivity
    s = s.lower()
    
    # Initialize a counter for vowels
    count = 0
    
    # Loop through each character in the string
    for char in s:
        # Check if the character is a vowel (including 'y' at the end of the word)
        if char in ['a', 'e', 'i', 'o', 'u', 'y' if s.index(char) == len(s) - 1 else None]:
            # Increment the vowel count
            count += 1
    
    # Return the total vowel count
    return count

# Test cases
print(vowels_count("abcde"))  # Expected: 2
print(vowels_count("ACEDY"))  # Expected: 3
print(vowels_count("Hello"))  # Expected: 2
print(vowels_count("AEIOU"))  # Expected: 5
print(vowels_count("BCDFG"))  # Expected: 0
print(vowels_count("yellow")) # Expected: 3
```

This Python script defines a function `vowels_count` that takes a string as input and returns the number of vowels in the string, considering 'y' as a vowel only when it's at the end of the word. The function uses a loop to iterate over each character in the string, checks if the character is a vowel, and increments a counter accordingly. The function returns the total vowel count. The script includes several test cases to demonstrate the function's correctness.