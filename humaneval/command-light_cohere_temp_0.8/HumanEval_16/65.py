```python
def count_distinct_characters(string: str) -> int:
    return len(set(string.lower()))
```

Here's a self-contained Python function that calculates the count of distinct characters in a given string, regardless of case. Using the `set` method, the characters are converted to lowercase to ensure uniqueness during set operation. The function then returns the unique character count in an integer.