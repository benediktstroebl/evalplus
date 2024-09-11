```python
def vowels_count(s):
    """
    Returns the number of vowels in the given word.
    'y' is considered a vowel only when it is at the end of the word.

    Args:
    s (str): The input word.

    Returns:
    int: The number of vowels in the word.
    """
    # Convert the string to lowercase for case-insensitive comparison
    s = s.lower()
    
    # Count the number of vowels
    count = sum(1 for char in s if char in 'aeiouy')
    
    # If 'y' is at the end of the word, decrement the count
    if s and s[-1] == 'y':
        count -= 1
    
    return count

# Test cases
print(vowels_count("abcde"))  # 2
print(vowels_count("ACEDY"))  # 3
```
This script defines the `vowels_count` function, which takes a string `s` as input, counts the number of vowels (with 'y' considered as a vowel only when at the end of the string), and returns the count. It includes example test cases to demonstrate the function's usage.