```python
def count_distinct_characters(string: str) -> int:
    return len(set(string.lower()))
```
This Python code defines a function called `count_distinct_characters`, designed to determine the number of unique characters, regardless of their case, in a given string. The function utilizes the `set()` and `lower()` methods along with `len()` to achieve this result. 

This function is self-contained and can be used to solve the problem of counting unique characters in a string, passing the string as an argument to the function.