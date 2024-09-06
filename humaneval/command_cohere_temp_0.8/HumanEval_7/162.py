```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if substring in s]
```

This function takes a list of strings (`strings`) and a substring (`substring`) as input and returns a new list containing only the strings from the input list that contain the given substring. It uses a list comprehension, iterating over each string in `strings`, and adding those that contain `substring` to the new list.

This solution should address the problem statement and correctly solve the challenge of filtering strings based on a substring. Let me know if you would like me to explain any part of the code in more detail!