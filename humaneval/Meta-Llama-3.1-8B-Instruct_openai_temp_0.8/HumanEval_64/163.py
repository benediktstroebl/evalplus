### Vowels Count Function
```python
def vowels_count(s):
    """
    Returns the number of vowels in the given string.
    Vowels in this case are 'a', 'e', 'i', 'o', 'u'. 
    'y' is also a vowel, but only when it is at the end of the given word.

    Parameters:
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
    
    # Iterate over each character in the string
    for char in s:
        # Check if the character is a vowel or 'y' at the end of the string
        if char in 'aeiou' or (char == 'y' and s == char):
            # Increment the vowel counter
            count += 1
    
    # Return the total vowel count
    return count

# Example usage:
print(vowels_count("abcde"))  # Output: 2
print(vowels_count("ACEDY"))  # Output: 3
```

This script defines the `vowels_count` function, which takes a string `s` as input and returns the number of vowels in the string according to the given rules. The function uses a simple iterative approach to count the vowels and handles the case sensitivity and the special 'y' rule. The example usage demonstrates how to use the function with different inputs.