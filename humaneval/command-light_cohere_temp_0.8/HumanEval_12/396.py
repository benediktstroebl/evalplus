```python
def longest(strings: List[str]) -> Optional[str]:
    if not strings:
        return None
    else:
        return max(strings, key=len)

# Example usage
strings = ['a', 'bb', 'ccc']
longest_result = longest(strings)
print(longest_result)  # Output: 'ccc'
```

This function `longest` takes a list of strings as input and returns the longest string from the list. It uses the using the `max` function to find the maximum length of the strings and then returns the longest string.