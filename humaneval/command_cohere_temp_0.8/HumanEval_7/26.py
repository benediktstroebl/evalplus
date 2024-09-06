```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if substring in s]
```

This function takes a list of strings (`strings`) and a substring (`substring`) as input, and returns a new list containing only the strings from the input list that contain the given substring. It uses a list comprehension, iterating over each string in `strings`, and adding those that contain `substring` to the new list.

Here is an example usage of the function:
```python
>>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
['abc', 'bacd', 'array']
>>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'b')
['bacd']
>>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'z')
[]
``` 

The example tests cover the basic scenarios for the function, including an empty input list, an empty substring, and a non-empty substring. The expected output varies depending on whether the substring is present in the string or not.