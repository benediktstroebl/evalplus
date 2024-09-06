```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [strng for strng in strings if strng.startswith(prefix)]
```

This function takes a list of strings, `strings`, and a string, `prefix`, as input and returns a new list, `return_list`, which includes only the strings from the input list that start with the input prefix. The function uses a list comprehension, which is a concise way to create lists in Python.

The basic syntax for the list comprehension is:
```python
return_list = [expression for item in list if condition]
```

The component parts of the list comprehension are:
- **Expression**: This is the logic that gets executed for each string of the list to determine if it qualifies to be part of the return list. In our case, the expression is the string itself because we want all strings that meet the condition to be part of the return list.
- **Item**: This represents each element in the input list (strings) that we are iterating through.
- **Condition**: This is the filter condition, expressed in a boolean expression. Only items that satisfy the condition are included in the new list. In our case, the condition is whether the string starts with the prefix.

The function includes type hints, `List[str]` and `str`, to provide clarity on the expected input and output types, aiding in code readability and maintainability. 

This function efficiently filters the input list to only include strings that start with the specified prefix, providing a convenient solution for such string filtering tasks.