### Vowels Counter
#### Problem Statement
Write a function `vowels_count` which takes a string representing a word as input and returns the number of vowels in the string.
Vowels in this case are 'a', 'e', 'i', 'o', 'u'. Here, 'y' is also a vowel, but only when it is at the end of the given word.

### Solution

```python
def vowels_count(s):
    """
    Count the number of vowels in a given string.

    Args:
    s (str): The input string.

    Returns:
    int: The number of vowels in the string.

    Vowels in this case are 'a', 'e', 'i', 'o', 'u'. 'y' is also a vowel when it is at the end of the word.

    Example:
    >>> vowels_count("abcde")
    2
    >>> vowels_count("ACEDY")
    3
    """
    # Define the vowels
    vowels = 'aeiou'
    # Add 'y' as a vowel when it's at the end of the word
    if s and s[-1].lower() == 'y':
        vowels += 'y'
    # Initialize the count of vowels
    count = 0
    # Iterate over each character in the string
    for char in s.lower():
        # Check if the character is a vowel
        if char in vowels:
            # If it is, increment the count
            count += 1
    # Return the total count of vowels
    return count
```

### Example Usage

```python
print(vowels_count("abcde"))  # Output: 2
print(vowels_count("ACEDY"))  # Output: 3
print(vowels_count("hello"))  # Output: 2
print(vowels_count("y"))      # Output: 1
```