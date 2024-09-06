```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [strng for strng in strings if strng.startswith(prefix)]
```

This function takes a list of strings, `strings`, and a string, `prefix`, as input and returns a new list, `return_list`, which includes only the strings from the input list that start with the input prefix. The function uses a list comprehension, which is a concise way to create a new list by performing a transformation on each item in an existing list.

To use the `filter_by_prefix` function, you can simply call it with the appropriate input arguments, such as:
```python
result = filter_by_prefix(["abc", "bcd", "cde", "array"], "a")
print(result)  # Output: ['abc', 'array']
``` 

This will store a new list in the `result` variable, which includes only strings that start with the prefix "a". In this case, the output of the function is:
```python
['abc', 'array']
``` 

The function is also designed to handle empty input lists gracefully, as illustrated in the code snippet below:
```python
result = filter_by_prefix([], "a")
print(result)  # Output: []
``` 

In this case, the output is an empty list since the input list is empty. This is shown by the output:
```python
[]
```