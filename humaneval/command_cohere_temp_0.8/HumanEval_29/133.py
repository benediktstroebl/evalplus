```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```

This function takes a list of strings, `strings`, and a string, `prefix`, as input and returns a new list, `return_list`, which includes only the strings from the input list that start with the input prefix. The behaviour of the function is defined by the list of tests provided earlier. A usage example is also provided to demonstrate how to invoke the function and print the resulting list. 

Here is an example of how to use the `filter_by_prefix()` function:
```python
>>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
['abc', 'array']
``` 

This example demonstrates how to use the `filter_by_prefix()` function to filter a list of strings and returns a list containing only the strings that start with the specified prefix, which in this case is 'a'. 

The function provides a useful utility that can be readily used in various Python scripts and applications that require list filtering based on a common prefix.  It can be used as a building block for more complex data processing tasks that involve string manipulation and filtering.