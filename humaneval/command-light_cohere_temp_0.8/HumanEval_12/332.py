```python
def longest(strings: List[str]) -> Optional[str]:
    if not strings:
        return None
    return max(strings, key=len)

# Test case 1
strings = ['a', 'b', 'c']
result = longest(strings)
print(result)  # Output: 'a'

# Test case 2
strings = ['a', 'bb', 'ccc']
result = longest(strings)
print(result)  # Output: 'ccc'

# Test case 3
strings = []
result = longest(strings)
print(result)  # Output: None
```
This script defines a function `longest` that takes a list of strings as input and returns the longest string from the list, or `None` if the list is empty. The function uses the maximum sorting algorithm with the `len` function as the key to return the longest string.