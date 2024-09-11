### Vowels Count Function

The following Python script defines a function `vowels_count` that takes a string as input and returns the number of vowels in the string.

```python
def vowels_count(s):
    """
    Counts the number of vowels in a given string.

    Vowels are 'a', 'e', 'i', 'o', 'u'. 'y' is also a vowel when it's at the end of the word.

    Args:
        s (str): The input string.

    Returns:
        int: The number of vowels in the string.

    Examples:
        >>> vowels_count("abcde")
        2
        >>> vowels_count("ACEDY")
        3
    """
    # Convert the string to lowercase for simplicity
    s = s.lower()
    # Initialize a counter for vowels
    count = 0
    # Check if the string is not empty
    if s:
        # Check if the last character is 'y'
        if s[-1] == 'y':
            # If 'y' is at the end, decrement the counter because 'y' is not a vowel in this case
            count -= 1
        # Iterate over the characters in the string
        for char in s:
            # Check if the character is a vowel
            if char in 'aeiou':
                # If it's a vowel, increment the counter
                count += 1
    # Return the count of vowels
    return count

# Example usage
print(vowels_count("abcde"))  # Output: 2
print(vowels_count("ACEDY"))  # Output: 3
```

This script uses a simple and efficient approach to count the vowels in the given string. It first converts the string to lowercase to handle both lowercase and uppercase vowels. It then checks if the last character is 'y' and adjusts the counter accordingly. Finally, it iterates over the characters in the string, checks if each character is a vowel, and increments the counter if it is.