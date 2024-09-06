```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if substring in s]
```

This function takes a list of strings (`strings`) and a substring (`substring`) as input, and returns a new list containing only the strings from the input list that contain the given substring. It uses a list comprehension, iterating over each string in `strings`, and including only those strings that have the `substring` present. 

Here's an example of how you can use the function with a sample input:
```python
>>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
['abc', 'bacd', 'array']
```

This will return a list containing the strings 'abc', 'bacd', and 'array', as they all include the substring 'a'. 

This approach assumes the input list is already sorted or ordered in some way, as it's not specifically designed to handle duplicate substrings within a string in the list. 
If you expect the input list to contain duplicate substrings (especially within the same string), you might consider adjusting the approach, like adding a parameter for case sensitivity or considering the expected frequency of the substring. Picking the most appropriate approach depends on the specific use case and the characteristics of the input data.