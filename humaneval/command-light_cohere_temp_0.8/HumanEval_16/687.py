Here is a Python script with a self-contained function that counts the number of distinct characters in a given string, regardless of case:
```python
def count_distinct_characters(string: str) -> int:
    """
    Count the number of distinct characters in a string, ignoring case.
    """
    string = string.lower()  # All words = string.split(' ')
    unique_chars = set(word.lower() for word in words)
    return len(unique_chars)
```

This function uses the `set()` function to create a set of lowercase versions of the characters in the input string, then uses a list comprehension to iterate over each word in the string, converting it to lowercase using the `lower()` method, and using the `set()` function to create a set of lowercase versions of characters. The `len()` method is then used to count the number of unique characters in the set, which corresponds to the number of distinct characters in the original string.