```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```
The function uses the contains() method to check if each string in the list contains the substring. The list comprehension then creates a new list containing only the strings that satisfy this condition.

This approach has a few benefits:
- It's concise and self-contained. The function doesn't rely on any external variables or globally accessible variables. It's an pure solution that can be easily reused and doesn't pollute the global namespace.
- It follows the DRY (Don't Repeat Yourself) principle, which makes the code more maintainable and helps with better testing and debugging.