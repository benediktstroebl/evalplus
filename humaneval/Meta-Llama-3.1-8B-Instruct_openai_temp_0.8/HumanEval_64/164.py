```python
FIX = """
Add more test cases.
"""

def vowels_count(s):
    """
    Count the number of vowels in a given string.

    Vowels are 'a', 'e', 'i', 'o', 'u'. 'y' is considered a vowel when it's at the end of the word.

    Args:
        s (str): Input string.

    Returns:
        int: Number of vowels in the string.

    Examples:
        >>> vowels_count("abcde")
        2
        >>> vowels_count("ACEDY")
        3
    """
    s = s.lower()  # Convert string to lowercase for simplicity
    count = 0
    ends_with_y = s[-1] == 'y'  # Check if string ends with 'y'

    for char in s:
        if char in 'aeiou':
            count += 1
        elif char == 'y' and not ends_with_y:
            pass  # 'y' is not a vowel when it's not at the end of the word

    # Add 1 if string ends with 'y' because 'y' is a vowel
    if ends_with_y:
        count += 1

    return count

# Test cases
print(vowels_count("abcde"))  # 2
print(vowels_count("ACEDY"))  # 3
```

This Python script defines the `vowels_count` function as specified in the problem and provides example test cases. It uses a simple approach to count vowels in the string, converting it to lowercase for simplicity and handling the special case of 'y' at the end of the word.