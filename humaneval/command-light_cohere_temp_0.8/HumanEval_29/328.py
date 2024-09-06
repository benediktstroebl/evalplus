Here's a self-contained Python function that filters an input list of strings based on a given prefix:
```python
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```

The function uses a list comprehension to filter out strings that do not start with the given prefix. It returns a full list of strings that match the given prefix.

Here are some test cases that can be used to validate the function:
```python
# Test cases
strings = ["abc", "bcd", "cde", "a", "array", "x", "y"]
prefix = "a"

# Function call
result = filter_by_prefix(strings, prefix)

print(result)  # Output: ['abc', 'a', 'array']
```

This would print the list of strings that start with the specified prefix.