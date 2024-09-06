```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```

This function takes a list of strings, `strings`, and a string, `prefix`, as input and returns a new list, `return_list`, which includes only the strings from the original list that begin with the provided prefix. This is achieved using a list comprehension, filtering out the elements that have a prefix that doesn't match the `prefix` variable.

To use this function, you can import the module containing it, call the function with the appropriate arguments, and assign the return value to a variable. Here's an example:
```python
from my_module import filter_by_prefix

my_list = ['abc', 'bcd', 'cde', 'array']
my_prefix = 'a'
result_list = filter_by_prefix(my_list, my_prefix)
print(result_list)
```

This will output the following:
```
['abc', 'array']
```

This exemplifies the function's behavior, filtering the `my_list` to include only strings that start with the `my_prefix` value.