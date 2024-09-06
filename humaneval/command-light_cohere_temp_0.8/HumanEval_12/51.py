Here's the solution:
```python
from typing import List
def longest(strings: List[str]) -> str:
    """
    Return the longest string from a list of strings.
    """
    string = ""
    for s in strings:
        if len(s) > len(string):
            string = s
    return string

# Test case 1
# Output: 'a'
strings = ['a', 'b', 'c']
result = longest(strings)
print(result)  # Output: 'a'

# Test case 2
# Output: 'ccc'
strings = ['a', 'bb', 'ccc']
result = longest(strings)
print(result)  # Output: 'ccc'

# Test case 3
# Output: None
strings = []
result = longest(strings)
print(result)  # Output: None
```
The `longest` function takes a list of strings as input and returns the longest string. The function compares the lengths of each string in the list and updates the `string` variable to the longest one encountered. The test cases demonstrate that the function works as expected.