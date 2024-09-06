```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```

This function takes a list of strings, `strings`, and a string, `prefix`, as input and returns a new list, `List[str]`, that contains only the strings from the input list that start with the specified prefix. It uses a list comprehension to iterate through each string in the input list and checks if it starts with the specified prefix using the `startswith` function. If the string starts with the prefix, it is included in the resulting list.

Here's an example of how you can use the `filter_by_prefix` function to filter a list of strings that start with the prefix "foo":
```python
>>> filter_by_prefix(['foo', 'bar', 'foobar', 'baz', 'foobaz'], 'foo')
['foo', 'foobar', 'foobaz']
``` 

The result is a list that contains only the strings that start with the specified prefix, 'foo' in this case.