Here's the Python code that provides the self-contained solution to the problem:
```python
def count_distinct_characters(string: str) -> int:
    return len(set(string.lower()))
```

This code creates a function called `count_distinct_characters`, which takes a string as input and returns the number of distinct characters in that string, regardless of case. The function uses the string. Then, the set() function is used to create a set of all characters in the string, and the `len()` function is used to count the number of items in the set. Finally, the return value is the length of the set.