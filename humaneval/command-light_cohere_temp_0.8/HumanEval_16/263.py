Here is a self-contained Python script that solves the problem of counting the number of distinct characters in a given string, regardless of case:
```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string if c.isupper(c)})
```

This script provides a function, `count_distinct_characters`, which takes a string as input and returns the count of distinct characters in the string, regardless of case. The function uses a set-based approach with a generator expression to create a set of characters and then checks if each character is in the set using the `isupper()` method, which returns `True` if the character is in uppercase. 

The function then returns the count of distinct characters, which is the length of the set.