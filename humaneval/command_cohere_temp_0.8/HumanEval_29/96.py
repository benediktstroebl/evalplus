```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [strng for strng in strings if strng.startswith(prefix)]
```

This function takes a list of strings, `strings`, and a string, `prefix`, as input and returns a new list, `List[str]`, that includes only the strings from the input list that start with the input prefix. This is an example of how the function can be used:
```python
>>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
['abc', 'array']
``` 

The function uses a list comprehension with a conditional statement to filter the input list to return the desired results. This is a powerful Python feature to create concise and readable code blocks. 

This solution should address the problem and successfully pass the tests. Let me know if you would like me to explain any of the code in more detail.