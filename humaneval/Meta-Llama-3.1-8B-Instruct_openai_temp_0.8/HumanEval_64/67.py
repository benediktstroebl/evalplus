```python
def vowels_count(s):
    """
    This function takes a string as input and returns the count of vowels in the string.
    Vowels are 'a', 'e', 'i', 'o', 'u'. 'y' is also considered a vowel if it's at the end of the string.

    Parameters:
    s (str): The input string.

    Returns:
    int: The count of vowels in the string.

    Examples:
    >>> vowels_count("abcde")
    2
    >>> vowels_count("ACEDY")
    3
    """

    # Convert the string to lower case to simplify the check for vowels
    s = s.lower()

    # Count the vowels, considering 'y' as vowel if it's at the end of the string
    count = sum(1 for char in s[:-1] if char in 'aeiou') + (s[-1] == 'y' and s[-2] not in 'aeiou')

    return count

# Test the function
print(vowels_count("abcde"))  # Expected output: 2
print(vowels_count("ACEDY"))  # Expected output: 3
```

This script defines a function `vowels_count` that takes a string as input and returns the count of vowels in the string, considering 'y' as vowel if it's at the end of the string. The function converts the string to lower case to simplify the check for vowels. It then uses a generator expression to count the vowels, excluding the last character if it's 'y' and the second last character is not a vowel. The result is returned by the function.