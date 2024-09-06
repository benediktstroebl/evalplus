```python
from typing import List

def longest(strings: List[str]) -> str:
    """
    Out of list of strings, returns the longest one.
    """
    for string in strings:
        if len(string) > len(longest):
            longest = string
    return longest

# Test cases
strings = ['a', 'b', 'c']
longest_value = longest(strings)
print(f'Longest value: {longest_value}')

strings = ['a', 'bb', 'ccc']
longest_value = longest(strings)
print(f'Longest value: {longest_value}')

strings = []
longest_value = longest([strings])
print(f'Longest value: {longest_value}')

strings = ['a', 'bb', 'ccc']
longest_value = longest([strings[0]] + strings[1:] + strings[2])
print(f'Longest value: {longest_value}')
```

The function `longest` takes a list of strings and returns the longest string. It iterates over each string in the list and checks if the length of the current string is greater than the length of the current `longest` string. If this is true, it updates the `longest` variable with the current string.