```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```
This Python function, `filter_by_substring`, takes a list of strings and a substring as input. It uses the `contains` to iterate over the strings in the list and returns a new list that contains only the strings that contain the given substring. This function is an concise implementation that solves the problem of filtering out strings that contain a given substring. 

Remember to handle type hints and avoid general variable names to adhere to Python best practices.