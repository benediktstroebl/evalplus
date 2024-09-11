```python
def vowels_count(s):
    """
    Counts the number of vowels in a given string.

    Vowels in this case are 'a', 'e', 'i', 'o', 'u'. 'y' is also a vowel
    when it is at the end of the given word.

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
    # Convert the string to lowercase to make the function case-insensitive
    s = s.lower()
    
    # Initialize a counter for the vowels
    count = 0
    
    # Check if the string is not empty
    if s:
        # Check if the last character is 'y'
        if s[-1] == 'y':
            # If it is, decrement the count
            count -= 1
        # Check each character in the string if it's a vowel
        for char in s:
            if char in 'aeiou':
                # If it is, increment the count
                count += 1
    
    # Return the total count of vowels
    return count

# Test cases
print(vowels_count("abcde"))  # Expected output: 2
print(vowels_count("ACEDY"))  # Expected output: 3
```

This script uses a for loop to iterate over each character in the input string. If the character is a vowel or 'y' at the end of the string, it increments the count. If the string is not empty and the last character is 'y', it decrements the count. The function then returns the total count of vowels in the string.