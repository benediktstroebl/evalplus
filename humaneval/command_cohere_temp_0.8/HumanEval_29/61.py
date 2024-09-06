```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```

This function takes a list of strings, `strings`, and a string, `prefix`, as input and returns a new list, `List[str]`, containing only the strings from the input list that start with the input prefix. The behaviour is defined by the type hints: `List[str]` and the `return` statement. 

The prefix matching is done using Python's list comprehension and the `startswith()` string method. 

This approach gives a clear and concise solution to the problem, and the function is easily understandable by other developers with minimal clarification. 

 Markdown could be used to demonstrate usage of the function:
```
```python
strings = ['abc', 'bcd', 'cde', 'array']
prefix = 'a'
result = filter_by_prefix(strings, prefix)
print(result)
```
```
This would produce the following output:
```
['abc', 'array']
``` 

This shows the function, applied to the `strings` list, successfully filtering out elements that start with the given `prefix`.