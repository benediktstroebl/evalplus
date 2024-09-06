Here is a Python script with a self-contained function that solves the problem of counting the number of distinct characters in a given string, regardless of case:
```python
def count_distinct_characters(string: str) -> int:
    return len(set(string.lower()))
```
This script defines a function `count_distinct_characters` that takes a string as input and returns the number of distinct characters in the string, regardless of case. The function uses the string.s set() and lowercase version of the string, converting all characters to lowercase. Then, the len() function is used to count the number of unique characters in the lowercase string.