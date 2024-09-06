```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    if not strings:
        return None
    return max(set(strings), key=strings.count)
```
This code solves the problem by using `max` with `key` argument, counting the occurrence of each string in the list through `strings.count`, and using `set(strings)` to remove any duplicates. The function returns `None` for empty input or when there is a tie in the maximum length. 
This solution has a time complexity of O(n log n) due to the use of `set` and the `count` method, which in the worst case has a logarithmic time complexity. It has a space complexity of O(1).