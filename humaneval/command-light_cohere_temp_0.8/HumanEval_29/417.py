Here is a self-contained Python script that defines a function `filter_by_prefix` solving the given problem:

```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix """
    return [x for x in strings if x.startswith(prefix)]
```

This script provides a function that takes a list of strings and a prefix as input, and returns a new list that contains only the strings from the input list that start with the given prefix. It also provides test with several test cases to ensure the correctness of the `filter_by_prefix` function.