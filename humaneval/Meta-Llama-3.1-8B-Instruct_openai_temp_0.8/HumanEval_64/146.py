```python
def vowels_count(s):
    """
    This function takes a string representing a word as input and returns the number of vowels in the string.
    Vowels in this case are 'a', 'e', 'i', 'o', 'u'. 'y' is also a vowel when it is at the end of the given word.

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
    # Convert the string to lowercase to simplify vowel detection
    s = s.lower()
    
    # Initialize a counter for vowels
    count = 0
    
    # Check each character in the string
    for i, char in enumerate(s):
        # Check if the character is a vowel
        if char in 'aeiou':
            # If it is, increment the vowel counter
            count += 1
        elif char == 'y' and i == len(s) - 1:
            # If the character is 'y' and it's at the end of the string, increment the vowel counter
            count += 1
    
    # Return the total vowel count
    return count

# Test the function
print(vowels_count("abcde"))  # Output: 2
print(vowels_count("ACEDY"))  # Output: 3
print(vowels_count("hello"))  # Output: 2
print(vowels_count("aeiou"))  # Output: 5
```

This script defines a function `vowels_count` that takes a string as input and returns the number of vowels in the string, with 'y' being a vowel only when it's at the end of the string. It uses a for loop to iterate over each character in the string, and checks if the character is a vowel or 'y' at the end of the string. If it is, it increments a vowel counter. Finally, it returns the total vowel count.