Here's a self-contained Python function that counts the number of distinct characters in a given string:
```python
def count_distinct_characters(string):
    return len(set(string.lower()))
```
This function uses the `set()` function along with the `lower()` method to create a set of all lowercase characters in the string. The `len()` function then returns the number of elements in the set, which are distinct characters in the string.