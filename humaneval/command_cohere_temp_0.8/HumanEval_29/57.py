```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [strng for strng in strings if strng.startswith(prefix)]
```

This function takes a list of strings, `strings`, and a string, `prefix`, as input and returns a new list, `List[str]`, containing only the strings from the input list that start with the input prefix. The function uses a list comprehension, which is a concise way to create a new list by applying a condition to each element of the existing list. 

To use the function, you can import it into a Python script or interactive environment and call it with a list of strings and a desired prefix as follows: 

```python
import filter_by_prefix

# Example Usage:
my_list = ['abc', 'bcd', 'cde', 'array']
my_prefix = 'a'
result_list = filter_by_prefix.filter_by_prefix(my_list, my_prefix)
print(result_list)
``` 

This will output the following:
```python
['abc', 'array']
``` 

This demonstrates that the function is returning the correct output. Note that if no matches are found, an empty list will be returned.