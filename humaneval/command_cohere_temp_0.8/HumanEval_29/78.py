```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [strng for strng in strings if strng.startswith(prefix)]
```

This function takes a list of strings, `strings`, and a string, `prefix`, as input and returns a new list, `return_list`, which contains only the strings from the input list that start with the input prefix. The function uses a list comprehension, which is a concise way to create a new list by applying a condition to each element of the existing list. 

To use the `filter_by_prefix` function, you can import it into your code or define it in the same file where you plan to use it. Here's an example of how to use it:
```python
filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
```

The output of this code, based on the function's description, would be:
```
['abc', 'array']
```

This demonstrates that the function is correctly filtering out only those strings that start with the given prefix, which in this case is 'a'.