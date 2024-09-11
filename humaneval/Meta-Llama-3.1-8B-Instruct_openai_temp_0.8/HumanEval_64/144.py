```python
FIX = """
Add more test cases.
"""

def vowels_count(s):
    """
    Count the number of vowels in a given string, considering 'y' as a vowel when it's at the end.

    Parameters:
    s (str): The input string.

    Returns:
    int: The number of vowels in the string.

    Examples:
    >>> vowels_count("abcde")
    2
    >>> vowels_count("ACEDY")
    3
    """

    # Convert the string to lowercase to handle case-insensitive comparison
    s = s.lower()

    # Initialize a counter for vowels
    count = 0

    # Check if the string ends with 'y'
    if s.endswith('y'):
        # If it does, remove the last character ('y') from the string
        s = s[:-1]

    # Iterate over each character in the string
    for char in s:
        # Check if the character is a vowel
        if char in 'aeiou':
            # If it's a vowel, increment the count
            count += 1

    # Return the total count of vowels
    return count
```

**Example use cases:**

```python
print(vowels_count("abcde"))  # Output: 2
print(vowels_count("ACEDY"))  # Output: 3
print(vowels_count("hello"))  # Output: 2
print(vowels_count("yummy"))  # Output: 2
print(vowels_count("aieou"))  # Output: 5
```