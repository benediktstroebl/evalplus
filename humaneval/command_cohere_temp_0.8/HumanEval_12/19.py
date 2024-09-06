```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    if not strings:
        return None
    elif len(set(strings)) == 1:
        return strings[0]
    return max(strings, key=len)
```
This Python script defines a function called longest in the above Markdown code block. The function takes a list of strings, `strings`, as input, and returns the longest string in the list. If the list contains multiple strings of the same length, it returns the first one. If the list is empty, it returns `None`. 

Here's a breakdown of what the function does:
1. It starts by checking if the `strings` list is empty. If it is, it returns `None`, as there are no strings to consider.
2. Next, it checks if there's only one unique string in the list. If so, it returns the only string because, by default, `max` with a custom `key` function only returns the first element of the `iterable` when its `key` returns the same value for multiple elements, which is the behavior we want for strings of equal length.
3. If there are multiple unique strings or multiple strings of equal length, it uses the `max` function with a custom key function to compare the strings based on their length. It retrieves the longest string, or the first one if there are multiple longest strings, and returns it.

The function is designed to be self-contained and easy to use, following the problem statement and test scenarios provided. You can use it as a standalone function in your Python scripts to solve the problem efficiently.