```python
from typing import List
def longest(strings: List[str]):
    """
    Returns the longest string in the list of strings.
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    """
    return max(strings, key=len)

# Example of input and output
input_strings = ['a', 'bb', 'ccc']
print(longest(input_strings))  # Output: 'ccc'
```

This function accepts a list of strings and returns the longest string from that list. We utilize the max function with the key argument set to the length. The result will be the string in the list with the longest length. The test cases pass successfully as well.