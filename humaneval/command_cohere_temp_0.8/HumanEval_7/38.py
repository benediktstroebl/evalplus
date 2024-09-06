```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if substring in s]
```

This code defines a function `filter_by_substring` that takes in a list of strings `strings` and a substring `substring` as input and returns a new list of strings that contain the specified substring. The function uses a list comprehension, iterating over each string in `strings`, and including only those that contain the substring `substring`. This is a common task in programming, especially for text analysis, automation, or string manipulation. 

This solution is testable and reusable, making it a good choice in a software development context. The function is also relatively efficient because it uses Python's built-in list comprehension, which iterates over the list once and doesn't alter the original list. 

The solution adheres to best practices in Python because it uses the `typing` module to declare the input parameter as `List[str]` and utilizes concise and readable one-liner list comprehension with a conditional statement. Furthermore, the function is documented with a docstring that explains its purpose, inputs, and expected behavior, enhancing readability and making it easier for potential users or maintainers to work with.