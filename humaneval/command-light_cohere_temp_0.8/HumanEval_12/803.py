Here's a self-contained Python function that returns the longest string from a list of strings:
```python
def longest(strings: List[str]) -> str:
    if not strings:
        return None
    return max(strings, key=len)
```

This code defines a function called longest that takes a list of strings as input and returns the longest string from that list. It checks if the fact input list is empty, in which case it returns None. Otherwise, it uses the maximum function with the `len` function as the key argument to find the maximum length among all the strings in the list.