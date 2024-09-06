```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if substring in s]
```

This code takes advantage of list comprehension to filter strings in the list that contain the given substring. It also adheres to Python's type hinting using the `typing` module. This helps provide better documentation and enable richer static type checking by tools such as Pyright. 

Such functional programming style, combined with type hinting, leads to a clean, easily understandable, and maintainable code. 

Thank you for prompting an opportunity to highlight the benefits of type hinting and functional style in Python. Please let me know if you'd like me to elaborate on any of the technologies involved or provide more examples of their application.