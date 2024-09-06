```python
from typing import List
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```
Here's a self-contained Python script that defines a function `filter_by_prefix` which filters an input list of strings based on whether their prefixes match a given prefix.  The function utilizes the basic list comprehension and the `startswith` method from the string module to achieve this.