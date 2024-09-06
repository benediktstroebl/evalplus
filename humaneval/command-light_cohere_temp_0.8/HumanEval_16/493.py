Here's the self-contained Python script with a function that counts the number of distinct characters in a given string, regardless of case:
```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string.info(lowercase=True) if c not in string.info('uppercase=True')})

# Test cases
assert count_distinct_characters('xyzXYZ') == 3
assert count_distinct_characters('Jerry') == 4
```
This script defines a function `count_distinct_characters` that takes a string as input and calculates the number of distinct characters using a dictionary comprehension with `lowercase=True` and `uppercase=True` to ensure uniqueness regardless of case. The test cases demonstrate the basic usage of the function. The `assert` statements are used to check if the function's output is correct for the given input.