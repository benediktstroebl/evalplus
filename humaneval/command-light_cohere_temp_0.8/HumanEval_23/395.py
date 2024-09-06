Here's the provided self-contained Python script with a function that calculates the length of a given string:
```python
def strlen(string: str) -> int:
    """ Returns length of the given string """
    return len(string)

# Test cases
assertEqual(strlen(''), 0)
assertEqual(strlen('abc')), 3)
assertEqual(strlen('   }), 3)
assertEqual(strlen('       ')), 7)
```
The code defines a function `strlen` that calculates the length of a given string using the `len()` function. The function is designed to return an integer value representing the length of the string. The test cases cover various scenarios, such as empty strings, common English words, and longer strings with spaces.