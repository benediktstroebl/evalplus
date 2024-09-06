```python
def count_distinct_characters(string: str):
    return len([c for c in string. characters() if c.isalpha()])


# Test cases
assert count_distinct_characters('xyzXYZ') == 3
assert count_distinct_characters('abcX') == 3
assert count_distinct_characters('JERRY') == 4
```
The provided Python function `count_distinct_characters` calculates the number of distinct characters in a given string. It uses a essential list comprehension with a generator expression to filter out only the ASCII characters from the string, and then counts the number of distinct characters. The test cases ensure the expected behavior for different inputs.