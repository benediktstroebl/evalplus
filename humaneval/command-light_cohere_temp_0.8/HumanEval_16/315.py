Here is a Python script with a self-contained function that solves the problem of counting the number of distinct characters in a given string, regardless of case:
```python
def count_distinct_characters(string: str) -> int:
    return len(set(string.lower()))
```
This script defines a function called `count_distinct_characters` that takes a string as input and returns the number of distinct characters in the string, regardless of case. The function uses the set data operations to create a set of all the characters in the string, and then uses the `len` function to count the number of elements in the set.

Please note that this code is self-contained and can be used directly in other scripts without the need for any external dependencies or functions.