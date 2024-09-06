Here's the self-contained Python function that counts the distinct characters in a given string, regardless of case:
```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string.str.casefold})

``` 
# Example tests
>>> count_distinct_characters('xyzXYZ')
3
>>> count_distinct_characters('jerry')
4
``` 
This function efficiently uses a dictionary comprehension to identify distinct characters, and the length of this set of characters is returned.