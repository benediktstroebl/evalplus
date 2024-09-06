```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [strng for strng in strings if strng.startswith(prefix)]
```

This function takes a list of strings, `strings`, and a string, `prefix`, as input and returns a new list, `return_list`, which contains only the strings from `strings` that have the specified `prefix`. The list comprehension iterates through each string in `strings` and checks if it starts with the `prefix`. If it does, the string is included in the `return_list`. 

Here's an example of using the function with a sample input and an explanation of the behavior:
```python
>>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
['abc', 'array']
```

In this example, we have the list `['abc', 'bcd', 'cde', 'array']` and the prefix, ` 'a'`. The function returns only `['abc', 'array']`, because these are the only two elements in the list that start with the prefix `"a"`. 

The function behavior is defined by the list comprehension and the `startswith` method:
```python
return [strng for strng in strings if strng.startswith(prefix)]
```

This means that for each string, `strng`, in the `strings` list, if the `strng` starts with the `prefix`, then the string is included in the `return_list`. 

This approach has an time complexity of O(n) since it requires iterating through all the elements in the list once, and the startswith check can be done in constant time.