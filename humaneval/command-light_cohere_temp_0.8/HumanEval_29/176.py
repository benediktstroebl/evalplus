Here's the self-contained Python script with a function that filters markdown code based on a given prefix:
```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """Filter an input list of strings only for ones that start with a given prefix."""
    return [string for string in strings if string.startswith(prefix)]
```

The function uses a list comprehension to iterate through the input list of strings and filter out any that do not start with the given prefix. The function also includes a docstring that explains its purpose and functionality, which helps to improve code readability and provide clear documentation.