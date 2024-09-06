Certainly, here's a self-contained Python script that defines the `concatenate` function, which takes a list of strings and returns their concatenation into a single string.

```python
from typing import List

def concatenate(strings: List[str]) -> str:
    # Convert list of strings into a single string
    return ''.join(strings)

# Example usage
strings = ['a', 'b', 'c']
result = concatenate(strings)
print(result)  # Output: 'abc'
```

This code provides a function that concatenates a list of strings into a single string. 
It is self-contained and can be used as a standalone solution to the problem described.