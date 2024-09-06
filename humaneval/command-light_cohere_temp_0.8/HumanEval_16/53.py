Here is a Python script that contains a self-contained function that counts the number of distinct characters in a given string, regardless of case:
```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string if c.isupper(c)})
```

The code defines a function called `count_distinct_characters` that takes a string as input and returns an integer. The function uses a string `string` and iterates over each character `c`. It uses the `isupper` method to convert `c` to uppercase and checks if it is already a character. If it is not, the character is added to a set of characters. The set is then converted back to a string using `str.isupper(c)` and the number of distinct characters is returned.