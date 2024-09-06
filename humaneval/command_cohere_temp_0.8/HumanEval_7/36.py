```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if substring in string]
```

This function takes a list of strings (`strings`) and a substring (`substring`) as input, and returns a new list containing only the strings from the input list that contain the given substring. It uses a list comprehension, iterating over each string in `strings`, and including only those that contain the substring `substring`. This solution should align with the problem statement and the provided test cases. Let me know if you'd like to provide any additional details or outline specific test cases to ensure the function is fully vetted.