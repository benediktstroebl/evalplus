Here is a self-contained Python script that solves the problem of counting the number of distinct characters in a given string, regardless of case:
```python
def count_distinct_characters(string):
    return len(set(string.lower()))
```
This script defines a function 'count_distinct_characters' that takes a string as input and returns the count of distinct characters (without case sensitivity) in that string.