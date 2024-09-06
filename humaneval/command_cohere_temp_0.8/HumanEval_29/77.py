```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [strng for strng in strings if strng.startswith(prefix)]
```

This function takes a list of strings, `strings`, and a string, `prefix`, as input and returns a new list, `return_list`, which includes only the strings from the input list that begin with the input prefix. The function uses a list comprehension, which is a concise way to create lists in Python.

The basic syntax for the list comprehension is:
```python
return_list = [expression for item in list if condition]
```

The component parts of the list comprehension are:
- **Expression**: This is the content that is going to be added to the new list. In our case, this is the string from the input list.
- **Item**: This is the element of the original list you’re looping over. This is `strng` in our case.
- **Condition**: This is the test that is performed on the items as you loop over them. In our example, the condition is `strng.startswith(prefix)`. The `startswith()` method tests whether the `strng` starts with the `prefix` or not. 

The list comprehension is a powerful tool that allows you to quickly and easily process lists and create new lists based on existing lists. In this case, it helps us efficiently filter the desired strings from the input list based on the given prefix. 

This function is straightforward and minimalist, achieving the desired outcome of filtering strings efficiently. It can be easily understood and used by other users to solve the specific problem and potentially in other scenarios requiring string filtering. 

You can use this function in other programs to filter strings based on different prefixes as needed, making it a useful tool in your Python coding toolbox.