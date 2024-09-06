```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [strng for strng in strings if strng.startswith(prefix)]
```

This function takes a list of strings, `strings`, and a string, `prefix`, as input and returns a new list, `List[str]`, containing only the strings from the input list that start with the specified prefix. It uses a list comprehension to iterate through each string in the input list and check if it starts with the provided prefix using the `startswith` method. If a string starts with the prefix, it's included in the resulting list. If it doesn't, it's not included in the list. 

The function is designed to be concise and straightforward, making it easy to understand and use. 

Here is an example of how to use the function:
```python
>>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
['abc', 'array']
```

The example includes the list of strings and the prefix to be filtered. The expected outcome is a list of strings that start with the specified prefix. The function effectively delivers the desired result.  In this case, it returns a list containing only 'abc' and 'array', as they are the only strings that start with the 'a' prefix.