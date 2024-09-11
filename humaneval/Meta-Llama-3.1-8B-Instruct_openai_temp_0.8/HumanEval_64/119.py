```python
def vowels_count(s):
    """Write a function vowels_count which takes a string representing
    a word as input and returns the number of vowels in the string.
    Vowels in this case are 'a', 'e', 'i', 'o', 'u'. Here, 'y' is also a
    vowel, but only when it is at the end of the given word.

    Parameters:
    s (str): The input string

    Returns:
    int: The number of vowels in the string

    Example:
    >>> vowels_count("abcde")
    2
    >>> vowels_count("ACEDY")
    3
    """
    # Convert the string to lowercase to simplify the check for vowels
    s = s.lower()
    
    # Initialize a counter for vowels
    count = 0
    
    # Check if the last character is 'y'
    if s and s[-1] == 'y':
        # If the last character is 'y', increment the count
        count += 1
    
    # Iterate over the characters in the string
    for char in s:
        # Check if the character is a vowel
        if char in 'aeiou':
            # If the character is a vowel, increment the count
            count += 1
    
    # Return the total count of vowels
    return count
```

**Testing the function**

```python
print(vowels_count("abcde"))  # Expected output: 2
print(vowels_count("ACEDY"))  # Expected output: 3
print(vowels_count("hello"))  # Expected output: 2
print(vowels_count("world"))  # Expected output: 1
print(vowels_count("y"))      # Expected output: 1
print(vowels_count(""))       # Expected output: 0
```

This script defines a function `vowels_count` that counts the number of vowels in a given string, considering 'y' as a vowel only when it is at the end of the string. The function is then tested with various input strings.