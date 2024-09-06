```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [strng for strng in strings if strng.startswith(prefix)]
```

This function takes a list of strings, `strings`, and a string, `prefix`, as input and returns a new list, `return_list`, which includes only the strings from the input list that start with the input prefix. The function uses a list comprehension to iterate through each string in the input list and check if it starts with the input prefix. If it does, the string is included in the `return_list`. 

Here's an example of how you can use the function with a sample input list of strings and prefix:
```python
>>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
['abc', 'array']
```
In this example, the function is called with an input list of strings ['abc', 'bcd', 'cde', 'array'] and a prefix 'a'. The function returns a list that includes 'abc' and 'array', which are the strings in the input list that start with the 'a' prefix. 

The function includes type annotations using Python's typing module to show the expected inputs and return values. These type annotations can be useful for code readability and maintenance, especially in larger codebases or when multiple developers are working on a project. 

The function does not have a docstring in this response, unlike the initial problem statement. However, if you want to keep the docstring, I can modify the function to include it as well.