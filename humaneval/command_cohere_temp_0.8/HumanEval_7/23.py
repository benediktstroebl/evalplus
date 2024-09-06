```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if substring in s]
```

This function takes a list of strings (`strings`) and a substring (`substring`) as input, and returns a new list containing only the strings from the input list that contain the specified substring. It uses a list comprehension, iterating over each string in `strings`, and adding those that include the substring `substring` to the new list. 

This solution should address the problem presented in the markdown code block and should work for the example use cases provided there. Let me know if you'd like to further discuss any details or explore other approaches.