```python
# Define a constant string with the word "y" at the end
Y_AT_END = "ydkjfy"

def vowels_count(s):
    """Write a function vowels_count which takes a string representing
    a word as input and returns the number of vowels in the string.
    Vowels in this case are 'a', 'e', 'i', 'o', 'u'. Here, 'y' is also a
    vowel, but only when it is at the end of the given word.

    Example:
    >>> vowels_count("abcde")
    2
    >>> vowels_count("ACEDY")
    3
    """
    # Initialize a counter for vowels
    count = 0
    
    # Check if the input string ends with 'y'
    ends_with_y = s.endswith('y')
    
    # Iterate through each character in the input string
    for char in s.lower():
        # Check if the character is a vowel or ends with 'y' when it's supposed to be
        if char in 'aeiou' or (char == 'y' and ends_with_y):
            # If the character is a vowel, increment the counter
            count += 1
            
    # Return the total number of vowels found
    return count

# Example usage
print(vowels_count("abcde"))  # Expected output: 2
print(vowels_count("ACEDY"))  # Expected output: 3
```

This script defines a `vowels_count` function that counts the number of vowels in a string, taking into account the special case where 'y' is a vowel only when it's at the end of the string. It uses the `str.lower()` method to ensure the function is case-insensitive and checks for the 'y' at the end of the string using the `str.endswith()` method. The function iterates through each character in the input string, counting the vowels, and returns the total number of vowels found.