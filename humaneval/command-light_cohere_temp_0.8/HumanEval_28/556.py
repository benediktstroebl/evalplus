```python
from typing import List
def concatenate(strings: List[str]) -> str:
    return ''.join(''.join(strings) if strings else '')

# Example usage:
strings = ['a', 'b', 'c']
result = concatenate(strings)
print(result)  # Output: 'abc'

```
This function concatenate takes a list of strings as input and returns a single string formed by concatenating the strings. We use the underwater join to make a single string without adding extra newline characters. The function is tested with a sample input, and the output is displayed.