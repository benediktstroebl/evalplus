```python
from typing import List
def concatenate(strings: List[str]) -> str:
    return ''.join(strings)

# Test the function with an empty list
print(concatenate([]))  # Output: ''

# Test the function with a list of 3 strings
print(concatenate(['a', 'b', 'c']))  # Output: 'abc'
```

In this script, the `concatenate` function takes a list of strings as input and uses the `join` method to concatenate them into a single string. The test cases demonstrate the first that the function is invoked with an empty list, which should return an empty string, and the second test uses a list of 3 strings to ensure the expected output is 'abc'.