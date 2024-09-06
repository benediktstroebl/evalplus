```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [strng for strng in strings if strng.startswith(prefix)]
```

This function takes a list of strings, `strings`, and a string, `prefix`, as input and returns a new list, `return_list`, which includes only the strings from the input list that start with the input prefix.

The function utilizes list comprehension, enhanced by the `startswith` method, to effectively filter out the desired strings from the input list. 

To demonstrate the function, here's an example of usage: 
```python
print(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a'))
```
This will output the list `['abc', 'array']`, as these are the only strings that start with the 'a' prefix from the input list. 

You can further verify the correctness of the function by writing additional test cases in the code block. For example: 
```python
print(filter_by_prefix([], 'a'))  # This will output: []
print(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'array'))  # This will output: ['array']
``` 
This provides an extensive check on the functionality of the function.