```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if substring in s]
```

This Python script defines a function called `filter_by_substring` that takes two arguments: a list of strings (`strings`) and a substring (`substring`). The function returns a new list containing only the strings from the input list that contain the specified substring. This is accomplished using a list comprehension, coupled with a generator expression, that filters elements based on the condition `substring in s`. 
```python
# Test code
>>> filter_by_substring([], 'a')
[]
>>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
['abc', 'bacd', 'array']
``` 
The test cases provided in the original problem demonstrate how the function handles empty input lists and applies the filtering correctly. 
This approach has a time complexity of `O(n)` since it requires iterating through each element in the list once.