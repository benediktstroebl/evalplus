```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string.count(c)} -sum()
```
This function calculates the number of distinct characters in a given string, regardless of case, using the `count()` function to collect unique characters and the `sum()` function to count them. 
The resulting count of distinct characters is then returned.