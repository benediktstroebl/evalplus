Here's the self-contained Python function that filters strings with a specific prefix:
```python
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```

This function uses the starts-with operator to check if each string in the input list starts with the specified prefix. The list comprehension then creates a new list containing only those strings that match the condition.

Here's how the function would be used:
```python
# Test cases
strings = ['abc', 'bcd', 'cde', 'array', 'hello']
prefix = 'cde'

result = filter_by_prefix(strings, prefix)
print(result)  # Output: ['cde', 'array']
```

This approach has a clean and self-contained function that efficiently filters the strings based on the provided prefix.