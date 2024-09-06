```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```
This function takes two inputs: a list of strings and a substring. It returns a specific list of strings from the input list that contain the given substring. The function uses the `contains` to iterate over the strings and the substring, and checks if each string contains the substring using the `contains` function.