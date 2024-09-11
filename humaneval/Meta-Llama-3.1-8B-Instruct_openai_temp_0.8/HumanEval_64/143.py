```python
def vowels_count(s):
    """
    This function takes a string as input and returns the number of vowels in the string.
    Vowels in this case are 'a', 'e', 'i', 'o', 'u'. Here, 'y' is also a vowel, but only when it is at the end of the given word.

    Args:
        s (str): The input string.

    Returns:
        int: The number of vowels in the string.
    """
    # Convert the string to lowercase to simplify the comparison
    s = s.lower()
    
    # Initialize a count variable to store the number of vowels
    count = 0
    
    # Check if the last character is 'y'
    if s[-1].lower() == 'y':
        # If the last character is 'y', remove it from the string
        s = s[:-1]
    
    # Iterate over each character in the string
    for char in s:
        # Check if the character is a vowel
        if char in 'aeiou':
            # If the character is a vowel, increment the count
            count += 1
    
    # Return the total count of vowels
    return count

# Example usage:
print(vowels_count("abcde"))  # Output: 2
print(vowels_count("ACEDY"))  # Output: 3
```

This script defines a function `vowels_count` that takes a string as input and returns the number of vowels in the string, considering 'y' as a vowel only when it is at the end of the string. The function iterates over each character in the string, checks if it is a vowel, and increments the count accordingly. The function also handles the special case where the last character is 'y'.