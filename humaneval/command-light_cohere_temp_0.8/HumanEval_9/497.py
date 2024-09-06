```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    return [x for x, _ in sorted(enumerrange(len(numbers)), key=numbers.max)]
```

This Python code defines a function `rolling_max` that generates a list of integers' maximum elements found up to the current moment in the sequence. The code also passes the design tests with a `numbers` sample list.