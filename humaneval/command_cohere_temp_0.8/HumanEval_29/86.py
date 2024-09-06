```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [strng for strng in strings if strng.startswith(prefix)]
```

This function takes a list of strings, `strings`, and a string, `prefix`, as input and returns a new list, `return_list`, which contains only the strings from `strings` that have the specified `prefix`. The list comprehension runs through each string in `strings` and returns those that start with the input `prefix`. 

Here's an example of how you can use the function by filtering a list of strings to include only those that start with the prefix "a":
```python
assert filter_by_prefix(
    ['abc', 'bcd', 'cde', 'array'], 
    'a'
) == ['abc', 'array']
```

This would return a list of strings that start with the prefix "a" which in this case is ['abc', 'array']. 

Such a function could have many practical applications in software development. For example, with this function, you could easily filter through log files to identify those entries that relate to a certain type of event. Or it could be used to process a list of files in a directory to those that pertain to a specific project or have a particular type of extension, and so on.