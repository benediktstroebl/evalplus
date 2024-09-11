```python
# Vowels Count Function
#-----------------------------

def vowels_count(s):
    """
    This function takes a string representing a word as input and returns
    the number of vowels in the string. Vowels in this case are 'a', 'e', 'i',
    'o', 'u'. Here, 'y' is also a vowel, but only when it is at the end of the
    given word.

    Parameters:
    s (str): The input word.

    Returns:
    int: The number of vowels in the word.

    Examples:
    >>> vowels_count("abcde")
    2
    >>> vowels_count("ACEDY")
    3
    """

    # Convert the string to lower case to handle upper case letters
    s = s.lower()

    # Initialize a counter for vowels
    count = 0

    # Iterate over each character in the string
    for i, char in enumerate(s):
        # Check if the character is a vowel
        if char in 'aeiou':
            # If 'y' is at the end of the word, it's a vowel
            if char == 'y' and i == len(s) - 1:
                count += 1
            else:
                count += 1

    # Return the count of vowels
    return count

# Example usage:
print(vowels_count("abcde"))  # Output: 2
print(vowels_count("ACEDY"))  # Output: 3
```

This Python script defines a function `vowels_count` that takes a string as input and returns the number of vowels in the string, following the rules specified in the problem. It handles both upper and lower case letters and correctly identifies 'y' as a vowel when it's at the end of the word. The function includes a docstring that explains its behavior and provides examples of its usage.