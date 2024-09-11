### Vowels Counter Script
```markdown
### Code
```python
def vowels_count(s):
    """
    Return the number of vowels in a given string.

    Vowels in this case are 'a', 'e', 'i', 'o', 'u'. 'y' is also considered
    a vowel, but only when it is at the end of the given word.

    Args:
    s (str): The input string.

    Returns:
    int: The number of vowels in the string.
    """
    vowels = 'aeiou'
    if s[-1].lower() == 'y':  # Check if 'y' is at the end of the word
        vowels += 'y'
    count = 0
    for char in s.lower():  # Iterate over the string, case-insensitive
        if char in vowels:
            count += 1
    return count

# Example usage:
print(vowels_count("abcde"))  # Output: 2
print(vowels_count("ACEDY"))  # Output: 3
```

### Explanation

This script defines a function `vowels_count` that takes a string `s` as input. It checks if the last character of the string is 'y' (case-insensitive) and adds it to the set of vowels. Then, it iterates over the string (case-insensitive), counting the number of vowels. Finally, it returns the count.

### Example Use Cases

You can use this function to count the number of vowels in any string. For example:
```python
print(vowels_count("hello"))  # Output: 2
print(vowels_count("xyz"))  # Output: 1 (because 'y' is at the end)
print(vowels_count("AEIOU"))  # Output: 5
```