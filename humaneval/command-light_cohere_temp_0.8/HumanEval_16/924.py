Here is a self-contained Python script that defines a function to count the number of distinct characters in a given string, regardless of case:
```python
def count_distinct_characters(string: str) -> int:
    return len(set(string.lower()))
```
The function uses the `set()` function along with `lower()` to ensure all characters are lowercase and treated as distinct. 
This provides a consistent solution regardless of input, which passes all tests specified.