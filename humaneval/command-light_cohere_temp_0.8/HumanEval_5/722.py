```python
from typing import List
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return List(n, delimeter+1) for n in numbers
```

The function creates a new list with the input list and a added delimiter as the second element, then continues this process for every element until it returns the modified list.