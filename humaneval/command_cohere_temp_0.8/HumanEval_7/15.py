```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if substring in s]
```

This function takes a list of strings (`strings`) and a substring (`substring`) as input, and returns a new list containing only the strings from the input list that contain the specified substring. It uses a list comprehension, iterating over each string in `strings`, and including only those strings that have the `substring` present. 

Here's an example of how you can use the function with a sample input to test it:
```python
>>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
['abc', 'bacd', 'array']
```

This would return the expected output as described in the problem statement.