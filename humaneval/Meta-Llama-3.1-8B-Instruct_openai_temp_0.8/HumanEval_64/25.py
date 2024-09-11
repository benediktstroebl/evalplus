```python
def vowels_count(s):
    """
    This function counts the number of vowels in a given string.
    A vowel is any of 'a', 'e', 'i', 'o', 'u'. 'y' is considered a vowel
    only when it's at the end of the word.

    Args:
        s (str): The input string.

    Returns:
        int: The count of vowels in the string.

    Examples:
        >>> vowels_count("abcde")
        2
        >>> vowels_count("ACEDY")
        3
    """

    # Convert the string to lowercase to simplify the check for vowels
    s = s.lower()
    
    # Initialize count of vowels
    count = 0
    
    # Check each character in the string
    for i in range(len(s)):
        # Check if the character is a vowel
        if s[i] in 'aeiou':
            # If it's a vowel, increment the count
            count += 1
        # Check if the character is 'y' and it's at the end of the string
        elif s[i] == 'y' and i == len(s) - 1:
            # If it's 'y' at the end, increment the count
            count += 1
    
    # Return the total count of vowels
    return count
```

You can use this function as follows:

```python
print(vowels_count("abcde"))  # Output: 2
print(vowels_count("ACEDY"))  # Output: 3
print(vowels_count("Hello World"))  # Output: 3
```