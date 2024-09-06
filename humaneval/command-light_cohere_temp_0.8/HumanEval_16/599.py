Here is a self-contained Python script that defines a function to count the number of distinct characters in a given string:
```python
def count_distinct_characters(string: str) -> int:
    return len(set(string.lower()))
```
This function employs the `set()` function along with the `lower()` method to remove case sensitivity and create a unique character set from the provided string. 

The `len()` function then simply returns the length of this set, which is the count of distinct characters. 
This is a simple and efficient way to solve the problem of counting unique characters in a string, regardless of case.