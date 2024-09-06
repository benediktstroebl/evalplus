```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```

This function takes a list of strings, `strings`, and a prefix, `prefix`, as input and returns a new list, `List[str]`, containing only the strings from the input list that start with the specified prefix. This is achieved using a list comprehension, filtering out the elements that have a prefix that doesn't match the desired prefix.

This solution directly implements the requirement posed in the Markdown code block and should yield the desired results for the given problem. It is concise and adheres to Python's best practices for string filtering. Additionally, it is scalable and adaptable to different list and prefix sizes without compromising performance.