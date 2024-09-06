Here is a self-contained Python function that solves the problem of finding the longest string in a list of strings:
```python
def longest(strings: List[str]) -> str:
    if not strings:
        return None
    return max(strings, key=len)
```
This function takes a list of strings as input and returns the longest string in that list. It checks if the quality of the input list is valid, and if it's empty, it returns None. If the list is not empty, it returns the string with the maximum length using the `max` function and the `key=len` argument to ensure the operation over-writes.

This solution follows the functional programming principle of single responsibility by encapsulating the logic of finding the longest string into a single function. It makes the code more readable and maintainable.