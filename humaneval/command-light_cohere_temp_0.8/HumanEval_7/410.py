Here's the self-contained Python script that solves the problem of filtering strings that contain a given substring:
```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string. contains substring(string)]
```
The provided Python script defines a function `filter_by_substring` that filters an input list of strings and returns a new list containing only those strings that contain a specified substring. The function uses the specific typing annotations to help clarify the intended function signature and the expected arguments.

This code follows the DRY principle and is self-contained, with no external dependencies. It efficiently filters the only relevant strings with the given substring, which is a common text manipulation operation.