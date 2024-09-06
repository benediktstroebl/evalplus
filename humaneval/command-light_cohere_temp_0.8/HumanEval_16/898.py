```python
def count_distinct_characters(string: str) -> int:
    return len(set(string.lower()))
```
This code defines a function `count_distinct_characters` that takes a string as input and returns the count of distinct characters in that string, regardless of their case. The function uses the lower() method to convert all characters to lowercase and then uses the `set()` and `len()` functions to count the number of unique characters and return that count. 

Please note that this function is self-contained and does not require any external variables or functions to solve the problem.