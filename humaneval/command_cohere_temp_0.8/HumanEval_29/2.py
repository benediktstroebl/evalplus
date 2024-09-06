```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```

This function takes a list of strings, `strings`, and a string, `prefix`, as input and returns a new list, `return_list`, which contains only the strings from `strings` that begin with `prefix`. It uses a list comprehension to iterate through each string in `strings` and returns the ones that start with the provided `prefix`. 

Here's an example of how you can use the `filter_by_prefix()` function with a sample input:
```python
>>> filter_by_prefix( ['abc', 'bcd', 'cde', 'array'], 'a')
['abc', 'array']
```
This would return a list containing only the strings 'abc' and 'array', filtered from the input list, as they both start with the specified prefix, 'a'.  This would be the expected output for the provided example in the markdown code block.