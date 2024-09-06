```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [strng for strng in strings if strng.startswith(prefix)]
```

This function takes a list of strings, `strings`, and a string, `prefix`, as input and returns a new list, `return_list`, which contains only the strings from `strings` that have the specified `prefix`. The resulting list is then typed as `List[str]` to avoid any confusion that may arise from the use of the generic type. 

Here is an example of how to use the function:
```python
>>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
['abc', 'array']
```
This example uses the function to filter the list of strings given, returning only those strings that begin with the specified prefix, 'a'. 

To further test this function, you may want to test it with an empty list or a list with strings that do not start with the given prefix. You can use the following examples:
```python
>>> filter_by_prefix([], 'a')
[]
>>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'z')
[]
``` 
These examples test for the function's behavior when an empty list or an irrelevant prefix is given.