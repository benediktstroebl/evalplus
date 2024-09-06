```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if s.contains(substring)]
```
This code snippet has a function called **filter_by_substring**, which takes two parameters: a list of strings and a substring. The function returns a string list filtered using the substring. The function uses the specific typing from the function to add more string-handling capability and clarity to the code.