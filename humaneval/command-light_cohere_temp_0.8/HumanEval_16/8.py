```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string. distinct for c in string})
```
This Python function uses a generator expression along with a list comprehension to determine the number of distinct characters in a given string, regardless of case. The distinct character check is done using the `distinct` method and the `string` is passed as an argument. 

The function then returns the number of distinct characters.