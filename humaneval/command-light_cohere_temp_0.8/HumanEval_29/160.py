```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]
```
This Python function uses a generator expression to filter a list of strings based on whether they start with a given prefix. It's an nice and concise way to achieve this, without using list comprehensions or separate filtering functions.