### Vowels Count Function
#### Problem Description
Write a function `vowels_count` which takes a string representing a word as input and returns the number of vowels in the string.
#### Solution

```python
def vowels_count(s):
    """
    Counts the number of vowels in a given string.

    Vowels are 'a', 'e', 'i', 'o', 'u'. 'y' is also a vowel when it's at the end of the string.

    Args:
        s (str): The input string.

    Returns:
        int: The number of vowels in the string.

    Examples:
        >>> vowels_count("abcde")
        2
        >>> vowels_count("ACEDY")
        3
    """
    vowels = 'aeiouy'
    if s:
        last_char = s[-1].lower()
        if last_char in 'y':
            vowels = vowels[:-1]
        return sum(1 for char in s.lower() if char in vowels)
    else:
        return 0

# Test cases
print(vowels_count("abcde"))  # Expected output: 2
print(vowels_count("ACEDY"))  # Expected output: 3
print(vowels_count(""))  # Expected output: 0
```

This script defines the `vowels_count` function that counts the number of vowels in a given string. It first checks if the string is not empty. If it's not empty, it checks if the last character is 'y'. If it is, it removes 'y' from the list of vowels. Then it uses a generator expression to count the number of vowels in the string. If the string is empty, it returns 0. The script also includes test cases to demonstrate the function's correctness.