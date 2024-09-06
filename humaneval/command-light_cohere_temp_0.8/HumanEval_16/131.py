```python
def count_distinct_characters(string: str) -> int:
    return len(set(string.lower()))
```

This code defines a function `count_distinct_characters` that calculates the number of distinct characters (case insensitive) in a given string. 

The function uses the `set()` function to create a set of characters from the input string, and then uses the `len()` function to count the number of elements in the set. 

To test the function, a few examples are provided that pass the function and print the result.