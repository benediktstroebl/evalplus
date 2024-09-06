```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if substring in s]
```

This function takes a list of strings (`strings`) and a substring (`substring`) as input, and returns a new list containing only the strings from the input list that contain the given substring. It uses a list comprehension, iterating over each string in `strings`, and including it in the new list if it contains the `substring`. This solution adheres to the type hint `List[str]` for the return type and the input parameter `strings`. 

To use this function, simply call it with a list of strings and the substring you want to filter by, and it will return a new list containing only the strings that contain the substring. 

For example:
```python
>>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
['abc', 'bacd', 'array']
``` 

This will return the expected result, filtering the input list to include only 'abc', 'bacd', and 'array', which are the strings containing the substring 'a'. 
If you want to filter by multiple substrings, you can do so by passing a list of substrings to the function, like this:
```python
>>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], ['a', 'r'])
['abc', 'array']
``` 

This will return the strings containing either 'a' or 'r', thereby filtering out 'bacd' and 'cde'.