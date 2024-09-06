Here is a self-contained Python function that solves the problem of returning the longest string from a list of strings:
```python
def longest(strings: List[str]) -> Optional[str]:
    if not strings:
        return None
    return max(strings, key=len)

# Test the function with different input
test_strings = ['a', 'b', 'c', 'bb', 'ccc']
result = longest(test_strings)
print(result)  # Output: 'ccc'
```

This code defines a Python function `longest` that takes a list of strings as input and returns the longest string. The function first checks if the input list is empty, in which case it returns `None`. Then, it uses the `max()` function along with the `key=len` argument to identify the longest string in the list, which has the maximum length.