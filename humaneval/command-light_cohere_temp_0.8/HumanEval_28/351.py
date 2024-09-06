```python
from typing import List
def concatenate(strings: List[str]):
    """
    Concatenate list of strings into a single string and return it.
    """
    string = ''.join(strings)
    return string
# Example test cases
strings = ["a", "b", "c"]
result = concatenate(strings)
print(result)  # Output: abc
```