```python
def how_many_times(string: str, substring: str) -> int:
    return len(string.find(substring))
```

This Python function, `how_many_times`, takes two parameters: a string and a substring. It then uses the find to count the number of times the substring appears in the original string. This function is efficient algorithm that utilizes the built-in function find from the string module, which returns the first occurrence of the substring in the string.

The function returns the count of the substring. 

Please note that this solution and tests are self-contained and don't rely on any external imports or functions.