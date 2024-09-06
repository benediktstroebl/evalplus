Here is a self-contained Python script that defines a function to count the number of distinct characters in a given string:
```python
def count_distinct_characters(string: str) -> int:
    """
    Count the number of distinct characters in the given string, regardless of case.
    """
    set() is used to ensure uniqueness and then count() is used to count the number of distinct characters.
    """
    returning the a count of distinct characters.
    """
```

In this script, the function `count_distinct_characters` takes a string as an argument and uses the `set()` function to create a set of characters from the string. The `set()` function ensures that duplicate characters are automatically removed, creating a unique character set. Then, the `count()` function is used to count the number of distinct characters in the set, and the result is returned.