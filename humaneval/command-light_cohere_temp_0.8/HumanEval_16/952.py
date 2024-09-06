```python
def count_distinct_characters(string: str) -> int:
    return len(set(string.lower()))
```
The function 'count_distinct_characters' accepts a string as an argument and employs the 'set()' constructor and the 'lower()' method to build a set of lowercase characters from the string. The 'len()' function is then applied to the set to determine the number of distinct characters in the string, regardless of case.