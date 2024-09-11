```python
def vowels_count(s):
    """
    Returns the number of vowels in the given string.
    'y' is considered a vowel only when it is at the end of the word.

    Args:
        s (str): The input string.

    Returns:
        int: The number of vowels in the string.
    """
    vowels = 'aeiou'
    has_y = s[-1].lower() == 'y'
    count = sum(1 for char in s.lower() if char in vowels)
    if has_y:
        count += 1
    return count

# Test the function
print(vowels_count("abcde"))  # Output: 2
print(vowels_count("ACEDY"))  # Output: 3
```

This script defines the `vowels_count` function as described in the problem statement and includes two example test cases to demonstrate its usage. The function uses a generator expression to count the occurrences of vowels in the given string, considering 'y' as a vowel only when it is at the end of the word.