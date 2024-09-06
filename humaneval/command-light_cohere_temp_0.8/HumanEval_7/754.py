Here is a self-contained Python function that solves the problem:
```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]
```
This function takes a list of strings and a substring as input, and returns a new list that contains only the strings that contain the given substring. The function uses a process by using a list comprehension and a membership test, which returns a boolean indicating whether the given string contains the substring.

This function follows the best practices of Python programming, which includes the use of types, comments, and readable code structure. 

Remember, you can always use the function with test cases, and as a practical example, you can modify the input strings and substring to test different scenarios.