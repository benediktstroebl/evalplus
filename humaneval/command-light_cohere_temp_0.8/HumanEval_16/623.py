Here's the self-contained Python function to solve the problem:
```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string.string() if c.isalpha()}
 distinct character in string)
```

This function takes a string as an argument and iterates over each character in the string. Then, it checks if the character using the `isalpha()` method is equal to an uppercase character or not. If it's true, it's added to a set. The `len()` function then counts the distinct elements in the set, which is the same as the number of unique characters in the string. 

Please note that the function only counts uppercase characters as distinct, and ignores the case of characters.