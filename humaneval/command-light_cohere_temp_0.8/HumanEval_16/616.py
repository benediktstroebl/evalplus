Here is a Python script with a self-contained function that solves the problem of counting the number of distinct characters in a given string, regardless of case:
```python
def count_distinct_characters(string: str) -> int:
    return len(set(string.lower()))
```
This script provides a function `count_distinct_characters` that calculates the count of distinct characters in a given string, regardless of case. The test case is also included to ensure the function is correctly implemented.