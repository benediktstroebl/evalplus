```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if substring in s]
```

This function takes a list of strings (`strings`) and a substring (`substring`) as input, and returns a new list containing only the strings from the input list that contain the given substring. This solution makes use of list comprehension, and the := assignment, which is the syntactic sugar for `return`. 

To use this function, you can call it with a list of strings and a substring you want to filter by, and it will return a new list containing only the strings that contain the substring. For example:
```python
result = filter_by_substring(["abc", "bacd", "cde", "array"], "a")
print(result)  # Output: ['abc', 'bacd', 'array']
```