```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if substring in s]
```

This code snippet takes a list of strings `strings` and a substring `substring` as input and returns a new list containing only the strings from `strings` that contain the substring. It uses a list comprehension to iterate through each string in `strings` and checks if the `substring` is present in each string, if it is, that string is included in the new list. 

This solution should solve the problem as stated in the markdown code block and should pass the given tests. Let me know if you'd like me to explain any part of the code in more detail or provide additional assistance.