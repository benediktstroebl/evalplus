```python
def count_distinct_characters(string: str):
    return len(set(string.lower()))
```
This Python code defines a function called `count_distinct_characters` that calculates the number of distinct characters in a given string, regardless of case. The string is passed as an parameter to the function and stored in the `string` variable. The `len` function is then called on this `string` and uses the `set()` function to create an unordered set of characters from the string, converted to lowercase using the `lower()` method. The `len` function then return the number of elements (distinct characters) in the set, which is the count of distinct characters in the original string.