Here is a self-contained Python script with a function that filters an input list of strings based on their prefix:
```python
from typing import List
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```
The function takes a list of strings and a prefix as input, and returns a new list containing only the strings from the input list that start with the given prefix. 

Here are some sample inputs and their corresponding outputs:
| Inputs:            | ['abc', 'bcd', 'cde', 'array', 'hello']
| prefix:           | 'cde'
| Output:             | ['cde']

This function uses a list comprehension to iterate over each string in the input list. The condition tests if the string starts with the given prefix.