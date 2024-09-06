Here is a self-contained Python function that solves the problem of concatenating list of strings into a single string:
```python
def concatenate(strings: List[str]) -> str:
    return "".join(strings)

# Test case: Concatenate empty list
print(concatenate([]))  # Output: ""

# Test case: Concatenate list of strings
print(concatenate(['a', 'b', 'c']))  # Output: 'abc'
```

This function takes a list of strings as an argument and returns a single string by concatenating the strings in the list. It is a tests for both basic cases, and provides a clear and self-contained solution for the given problem.