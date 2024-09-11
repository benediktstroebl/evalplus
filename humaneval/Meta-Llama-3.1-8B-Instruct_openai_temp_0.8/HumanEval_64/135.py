### Vowels Count Function

```python
def vowels_count(s):
    """
    This function takes a string representing a word as input and returns 
    the number of vowels in the string.
    
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
    
    # Convert the string to lowercase to simplify the vowel check
    s = s.lower()
    
    # Initialize a counter for the number of vowels
    vowel_count = 0
    
    # Iterate over each character in the string
    for i, char in enumerate(s):
        # Check if the character is a vowel or 'y' at the end of the string
        if char in 'aeiou' or (char == 'y' and i == len(s) - 1):
            # If the character is a vowel or 'y' at the end, increment the counter
            vowel_count += 1
    
    # Return the total count of vowels
    return vowel_count

# Test the function with example inputs
print(vowels_count("abcde"))  # Output: 2
print(vowels_count("ACEDY"))  # Output: 3
print(vowels_count("Hello World"))  # Output: 3
print(vowels_count("AEIOU"))  # Output: 5
print(vowels_count("bcdfg"))  # Output: 0
```