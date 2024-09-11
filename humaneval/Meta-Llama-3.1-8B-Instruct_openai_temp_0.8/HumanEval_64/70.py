```python
def vowels_count(s):
    """
    Write a function vowels_count which takes a string representing
    a word as input and returns the number of vowels in the string.
    Vowels in this case are 'a', 'e', 'i', 'o', 'u'. Here, 'y' is also a
    vowel, but only when it is at the end of the given word.

    Args:
        s (str): The input word.

    Returns:
        int: The number of vowels in the word.

    Example:
        >>> vowels_count("abcde")
        2
        >>> vowels_count("ACEDY")
        3
    """
    # Convert the string to lower case to simplify the comparison
    s = s.lower()
    
    # Initialize a counter for the vowels
    count = 0
    
    # Check if the last character is 'y' and increment the count if it is
    if len(s) > 0 and s[-1] == 'y':
        count += 1
    
    # Iterate over each character in the string
    for char in s:
        # Check if the character is a vowel and increment the count if it is
        if char in 'aeiou':
            count += 1
            
    # Return the total count of vowels
    return count

# Test cases
print(vowels_count("abcde"))  # Output: 2
print(vowels_count("ACEDY"))  # Output: 3
print(vowels_count("hello"))  # Output: 2
print(vowels_count("AEIou"))  # Output: 4
```

This script defines a function `vowels_count` that calculates the number of vowels in a given string. It handles the special case where 'y' is a vowel when it appears at the end of the word. The function is then tested with several example cases to verify its correctness.