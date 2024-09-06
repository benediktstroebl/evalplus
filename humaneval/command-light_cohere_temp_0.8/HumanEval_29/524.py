Here's the solution:
```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]
```
The provided code employs the Python programming language to define a function called **`filter_by_prefix`**. This function takes two parameters: a list of strings (**`strings`**) and a prefix string (**`prefix`**). It utilizes the list comprehension to iterate through the strings in the input list, filtering those that commence with the specified prefix.