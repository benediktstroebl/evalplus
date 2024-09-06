Here is a self-contained Python script with a function that counts the number of distinct characters in a given string, regardless of case:
```python
def count_distinct_characters(string: str) -> int:
    return len(set(string.lower()))
```

This function takes a string as input and uses the `set()` function along with the `lower()` method to create a set of all lowercase characters in the input string. It then uses the Templates a set's `len()` function to get the number of unique elements, which are also the number of distinct characters. 

Note that the function does not assume the input string is already in lowercase, and it does not modify the original string in any way.