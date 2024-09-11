```python
def vowels_count(s):
    """
    This function takes a string representing a word as input and returns
    the number of vowels in the string. Vowels in this case are 'a', 'e', 'i', 'o', 'u'.
    'y' is also a vowel, but only when it is at the end of the given word.

    Args:
        s (str): The input string.

    Returns:
        int: The number of vowels in the string.
    """
    # Convert the string to lowercase to simplify the vowel check
    s = s.lower()
    
    # Initialize a counter for the number of vowels
    count = 0
    
    # Check each character in the string
    for i, char in enumerate(s):
        # Check if the character is a vowel or 'y' at the end of the string
        if char in 'aeiou' or (char == 'y' and i == len(s) - 1):
            # If it's a vowel, increment the counter
            count += 1
    
    # Return the total count of vowels
    return count

# Example use cases:
print(vowels_count("abcde"))  # Output: 2
print(vowels_count("ACEDY"))  # Output: 3
print(vowels_count("hello"))  # Output: 2
print(vowels_count("world"))  # Output: 1
```

The above script defines the `vowels_count` function which takes a string `s` as input and returns the number of vowels in the string. The function converts the string to lowercase to simplify the vowel check, then iterates over each character in the string. It checks if the character is a vowel or 'y' at the end of the string, and if so, increments the vowel count. The script includes example use cases at the end to demonstrate the function's behavior.