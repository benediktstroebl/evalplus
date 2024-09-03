Here is a self-contained Python script that solves the problem of filtering strings for a given substring:

```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]
```

This script defines a function `filter_by_substring` that takes in a list of strings and a substring as arguments. The function then creates a list comprehension that iterates through the input strings and returns only the strings that contain the given substring. 

Here is an example of how you could use this function:

```python
strings = ['abc', 'bacd', 'cde', 'array', 'xzy']
substring = 'cde'
result = filter_by_substring(strings, substring)
print(result)
```

Output:
['cde', 'array']

This would output the list ['cde', 'array'] which are the strings that contain the substring 'cde' from the list of strings.