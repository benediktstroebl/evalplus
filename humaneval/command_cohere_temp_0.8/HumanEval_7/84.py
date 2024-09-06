```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if substring in s]
```

This code defines a function `filter_by_substring` that takes in a list of strings (`strings`) and a substring (`substring`) as input and returns a new list of strings that contain the specified substring. It uses a list comprehension, iterating over each string in `strings`, and including only those that contain the substring `substring`. 

This solution should pass the provided tests, as it correctly filters out strings that do not contain the given substring and returns those that do. 
```python
# Test Case 1
assert filter_by_substring([], 'a') == []

# Test Case 2
assert filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a') == ['abc', 'bacd', 'array']
```