```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [strng for strng in strings if strng.startswith(prefix)]
```

This function takes a list of strings, `strings`, and a string, `prefix`, as input and returns a new list, `return_list`, which contains only the strings from the input list that start with the given prefix. The syntax is straightforward, using a list comprehension with a conditional statement `if strng.startswith(prefix)`. The `startswith` method checks if the string starts with the supplied prefix, and the conditional statement acts as a filter to pass only the desired strings. 

To demonstrate the function, here is an example of usage: 
```python
print(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a'))
```
The above code prints out the list ['abc', 'array'], which are the only elements from the input list that start with the 'a' prefix. 

This function is easy to understand and use, and efficient since it eliminates the need for manual filtering, making it a valuable tool for solving this problem.