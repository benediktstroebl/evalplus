```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if substring in s]
```

This code takes advantage of list comprehension to filter strings in the list that contain the given substring. It also adheres to Python's type hinting using the `typing` module. This helps provide better documentation and enable richer static type checking by tools such as mypy. 

Such descriptive comments are helpful when marking code for easy understanding by other users or future self. They also help in proving correctness of the code indirectly through the process of "proof by explanation". This process enables developers to gain confidence in the code's behaviour by systematically explaining how it behaves and conforms to the given problem statement.