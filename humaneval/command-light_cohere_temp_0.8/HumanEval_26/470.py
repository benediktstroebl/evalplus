```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    return [num for num in numbers if num not in seen and num not in numbers[:seen.remove(num)])
```

This script defines a function called remove_duplicates, which takes a list of integers as an argument. It uses a method seen to create a set of the elements in the input list, then uses the built-in function remove(set()) to remove duplicates from the set. This results in a output being a list of the remaining elements that are not in the set or the original list.