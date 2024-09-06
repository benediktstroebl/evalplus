```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if substring in s]
```

This function takes a list of strings (`strings`) and a substring (`substring`) as input, and returns a new list containing only the strings from the input list that contain the given substring. This solution makes use of list comprehension, and the Python typing module is used to make the function more expressive and clarify the expected inputs. This function is applicable to various scenarios involving string filtering within lists.  The function is encapsulated in a self-contained code block, accessible as a module, and has detailed documentation for further understanding.