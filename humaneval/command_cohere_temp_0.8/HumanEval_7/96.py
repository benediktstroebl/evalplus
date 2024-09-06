```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if substring in string]
```

This function takes a list of strings (`strings`) and a substring (`substring`) as input and returns a new list containing only the strings from the input list that contain the given substring. It uses a list comprehension, iterating over each string in `strings`, and including it in the new list if it contains the `substring`. 

Here's an example of using the function with a sample input and an expected output:
```python
>>> filter_by_substring(=['abc', 'bacd', 'cde', 'array'], 'a')
['abc', 'bacd', 'array']
```

The above function can be invoked with two arguments: an input list of strings `'['abc', 'bacd', 'cde', 'array']'` and a substring `'a'`. The function then returns the expected output `'['abc', 'bacd', 'array']'`, as documented in the code snippet. 
If you encounter any difficulties understanding the solution or anything else, please don't hesitate to ask!