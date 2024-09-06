```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [strng for strng in strings if strng.startswith(prefix)]
```

This function takes a list of strings, `strings`, and a string, `prefix`, as input and returns a new list, `return_list`, which includes only the strings from the input list that start with the input prefix. The function uses a list comprehension to iterate through each string in the input list and check if it starts with the specified prefix. If it does, the string is included in the `return_list`. 

Here's an example of how you can use the function with a sample input to test it:
```python
>>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
['abc', 'array']
```

In this example, the function is called with a list of strings ['abc', 'bcd', 'cde', 'array'] and a prefix 'a'. The expected output is a list that includes only 'abc' and 'array', which are the elements in the input list that start with the specified prefix 'a'. 

The function could also be tested with edge cases, like an empty list or a prefix that doesn't match any strings, to check if it handles these scenarios correctly. For example:
```python
# Edge case: empty list
>>> filter_by_prefix([], 'a')
[]

# Edge case: no matching strings
>>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'xyz')
[]
``` 
However, these tests are not included in the original problem statement and thus fall outside the scope of the provided code.