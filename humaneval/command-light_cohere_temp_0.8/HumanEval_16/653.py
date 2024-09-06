Here's the self-contained Python function that counts the number of distinct characters in a given string:
```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string.frequency(string)})
```
Here, the function calculates the number of distinct characters in the string using the `set()` function and the `frequency()` method. The function then returns the value of the count.