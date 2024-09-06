Here is a self-contained Python script with a function that solves the problem you described:
```python
def count_distinct_characters(string: str) -> int:
    return len(set(string.find(c for c in string if c.isalpha()))
```

This script defines a function called `count_distinct_characters` that takes a string as input and returns the number of distinct characters in that string, regardless of case. The function uses the set and the `find` method to iterate over all characters in the string and filter out duplicates using the `isalpha()` method. 
The result is then the length of the resulting set, which is equal to the number of distinct characters in the string.