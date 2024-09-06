```python
from typing import List
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]
```
Here, the function uses a list comprehension to filter out any strings that do not start with the given prefix. This code is written in a clear, concise manner and follows good coding practices.