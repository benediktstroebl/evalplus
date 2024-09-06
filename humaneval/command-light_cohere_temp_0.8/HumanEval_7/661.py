```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if s.contains(substring)]
```
This Python code defines a function called `filter_by_substring`, which takes a list of strings and a substring as input and returns a new list containing only the strings from the input list that contain the given substring. The code uses the filter to find all occurrences of the substring within each string in the input list. 

It utilizes the `contains` keyword to convert the substring into a function call, allowing it to be a part of the `strings` list. The code uses a list comprehension to filter the strings based on whether they contain the substring.