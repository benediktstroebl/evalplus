```python
from typing import List
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]
```

This code implements a function **filter_by_prefix** that filters an input list of strings based on a given prefix. It uses the basic Python list comprehension with a lambda function to achieve this.

The function takes in two parameters: **strings** which is the list of strings to filter and **prefix** which is the prefix to search for. It returns a filtered list of strings that start with the given prefix.

Here's how the function is used with an example:

```python
print(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a'))
# ['abc', 'array']
```

This will print the list of strings that start with 'a', which in this case are 'abc' and 'array'.