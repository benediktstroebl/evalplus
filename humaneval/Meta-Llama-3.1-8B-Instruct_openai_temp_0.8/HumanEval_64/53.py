```python
def vowels_count(s):
    """
    This function returns the count of vowels in the given string.
    Vowels are 'a', 'e', 'i', 'o', 'u'. 'y' is also a vowel if it's at the end of the string.

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
    vowels = 'aeiou'
    s = s.lower()  # Convert the string to lowercase to simplify vowel checking
    if s and s[-1] == 'y':  # Check if the last character is 'y'
        vowels += 'y'  # Add 'y' to the set of vowels if it's at the end
    return sum(1 for char in s if char in vowels)  # Count the occurrences of vowels


# Test cases
print(vowels_count("abcde"))  # Expected output: 2
print(vowels_count("ACEDY"))  # Expected output: 3
```

This script defines a function `vowels_count` that takes a string `s` as input and returns the number of vowels in the string. The function checks if the last character is 'y', and if so, it treats 'y' as a vowel. It then counts the occurrences of 'a', 'e', 'i', 'o', 'u', and possibly 'y', in the string and returns the result. The test cases at the end of the script demonstrate the function's usage.