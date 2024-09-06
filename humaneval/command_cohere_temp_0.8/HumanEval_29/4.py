```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [strng for strng in strings if strng.startswith(prefix)]
```

This function takes a list of strings, `strings`, and a string, `prefix`, as input and returns a new list, `return_list`, which contains only the strings from `strings` that have the specified `prefix`. The resulting list is then typesafed according to the `List` datatype. 

The logic of the function is contained within a list comprehension, which is a common Python idiom for filtering elements in lists. 

For example, running the function with the following input:
```python
>>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
['abc', 'array']
```

will return a list that is filtered to contain only the elements 'abc' and 'array', which are the elements in the input list that have the prefix 'a'. 

This approach provides a straightforward solution to the problem, which is also easily understandable by developers new to the codebase. 

If needed, this function can also be modified to include additional functionality, such as case-insensitivity or further customization of the filter process, thereby adapting to whichever specific direction the requirements for this problem may evolve towards.