```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [strng for strng in strings if strng.startswith(prefix)]
```

This function takes a list of strings, `strings`, and a string, `prefix`, as input and returns a new list, `List[str]`, containing only the strings from the input list that start with the input prefix. It uses a list comprehension to iterate over each string in the input `strings`, and checks if it starts with the specified `prefix`, if so, it includes the string in the new list it is creating. The resulting list contains only the strings that have the desired prefix. 

The function is designed to be self-contained, meaning it can be dropped into any Python project, and it will work as expected without any additional dependencies or modifications. 

Here is an example of how to use the function:
```python
>>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
['abc', 'array']
```
This would return a list containing only those two strings from the input list that have the prefix "a". 

You can also easily test this function by calling it with different input lists and prefixes to verify it works as expected. 
```python
>>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'ar')
['array']

>>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'abc')
['abc']
``` 

As expected, the prefixes "ar" and "abc" match only the respective strings in the input list.