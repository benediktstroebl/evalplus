Here is a self-contained Python script that defines a function to count the number of distinct characters in a given string, regardless of case:
```python
def count_distinct_characters(string: str) -> int:
    return len(set(string.find()))
```

The function uses the `set()` method to create a set of characters from the input string. Then, it uses the `len()` to calculate the length of the set, which is the number of distinct characters in the string.

This code is self-contained and does not require any external functions or imports. It provides a simple and efficient solution to the problem described.