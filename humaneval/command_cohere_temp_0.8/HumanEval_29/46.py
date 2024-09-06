```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [strng for strng in strings if strng.startswith(prefix)]
```

This function takes a list of strings, `strings`, and a string, `prefix`, as input and returns a new list, `List[str]`, that includes only the strings from the input list that start with the input prefix. This is achieved using a list comprehension that iterates over each string in `strings` and returns the ones that start with `prefix` using the `startswith` function. 

Here is an example of how to use the function:
```python
>>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
['abc', 'array']
```

This would return a list that is filtered to include only the strings that start with the prefix "a", which in this case are "abc" and "array". 

This approach ensures readability and efficiency and enables the function to handle a variety of input scenarios, including handling empty input lists or lists with no strings starting with the given prefix, as depicted in the example usage provided alongside the function.