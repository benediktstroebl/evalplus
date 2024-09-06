```python
def count_distinct_characters(string: str) -> int:
    return len(set(string.lower()))
```
This Python function 'count_distinct_characters' accepts a string as input and returns the count of distinct characters, regardless of case, using the 'len' of the 'set' function and a 'lower' method. 
It successfully counts the distinct characters in the input and passes the test of providing the expected output for various inputs.