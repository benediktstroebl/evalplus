```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [strng for strng in strings if strng.startswith(prefix)]
```

This function takes a list of strings, `strings`, and a string, `prefix`, as input and returns a new list, `return_list`, which includes only the strings from the input list that begin with the input prefix. The function utilizes list comprehension and a boolean condition, `strng.startswith(prefix)`, to filter the list appropriately. 

To test this function, you can use the following code: 
```python
test_list = ['abc', 'bcd', 'cde', 'prefixed_string']
test_prefix = 'pre'

expect = ['abc', 'prefixed_string']

assert filter_by_prefix(test_list, test_prefix) == expect
```

The expected output should be `[ 'abc', 'prefixed_string' ]`.