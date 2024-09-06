```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [strng for strng in strings if strng.startswith(prefix)]
```

This function takes a list of strings, `strings`, and a string, `prefix`, as input and returns a new list, `List[str]`, that includes only the strings from the input list that start with the input prefix. The function uses a list comprehension, creating and returning a new list by applying a specified condition to each item in the original list.

To use the function, you can call it with a list of strings and a desired prefix as follows:
```python
input_strings = ['abc', 'bcd', 'cde', 'array']
input_prefix = 'a'
filtered_strings = filter_by_prefix(input_strings, input_prefix)
print(filtered_strings)  # Output: ['abc', 'array']
``` 

This will output a list containing only those strings from `input_strings` that have a prefix matching the `input_prefix`.