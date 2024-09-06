```python
from typing import List
def concatenate(strings: List[str]) -> str:
    return ''.join(strings)

# Tests
strings = ['a', 'b', 'c']
result = concatenate(strings)
print(result)  # Output: 'abc'
```
The provided Python code defines a function called `concatenate` that takes a list of strings as an argument and concatenates them into a single string. It uses the... `+join` method to create a new string by joining the strings together. The function is then tested with a sample input of strings ['a', 'b', 'c'], and the output is printed to verify the correctness of the function.

This is a self-contained function that can solve the problem of concatenating strings in a markdown code block.