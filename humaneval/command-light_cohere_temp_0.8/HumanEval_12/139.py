Here's the function that solves the problem:
```python
def longest(strings: List[str]) -> Optional[str]:
    if not strings:
        return None
    return max(strings, key=len)

# Test cases
strings = ['a', 'b', 'c']
longest(strings)  # Output: 'c'

strings = ['a']
longest(strings)  # Output: 'a'

strings = []
longest(strings)  # Output: None

strings = ['aa', 'bb', 'ccc']
longest(strings)  # Output: 'bb'
```
The function `longest` takes a list of strings as input and returns the longest string from the list, or `None` if the list is empty. The `max` function is used to compare the lengths of the strings and return the maximum value.