```python
def vowels_count(s):
    """Write a function vowels_count which takes a string representing
    a word as input and returns the number of vowels in the string.
    Vowels in this case are 'a', 'e', 'i', 'o', 'u'. Here, 'y' is also a
    vowel, but only when it is at the end of the given word.

    Parameters:
    s (str): Input string

    Returns:
    int: Number of vowels in the string

    Example:
    >>> vowels_count("abcde")
    2
    >>> vowels_count("ACEDY")
    3
    """
    # Convert the string to lowercase to handle both uppercase and lowercase letters
    s = s.lower()
    # Initialize a counter for vowels
    count = 0
    # Check if the last character of the string is 'y'
    if s and s[-1] == 'y':
        # If 'y' is at the end, increment the counter
        count += 1
    # Iterate over each character in the string
    for char in s:
        # Check if the character is a vowel
        if char in 'aeiou':
            # If it's a vowel, increment the counter
            count += 1
    # Return the total count of vowels
    return count

# Test the function
print(vowels_count("abcde"))  # Output: 2
print(vowels_count("ACEDY"))  # Output: 3
```
This script defines the `vowels_count` function, which takes a string as input and returns the number of vowels in the string. It handles both uppercase and lowercase letters by converting the input string to lowercase. It also checks if the last character of the string is 'y' and increments the counter if it is. The function then iterates over each character in the string, checking if it's a vowel, and increments the counter if it is. Finally, the function returns the total count of vowels.