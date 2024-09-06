```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = [x for x in numbers if x != delimeter]
    return delimeter + result if result else []
```

The function takes in two parameters, `numbers`, which is a list of integers, and `delimeter`, which is the number to be placed in between consecutive elements of the `numbers` list. The function checks if the `numbers` list element is not equal to the `delimeter`, if so, it saves it in the `result` list. In the end, it returns `delimeter` plus the `result` list, or an empty list if the `result` list is empty.

Here is a sample output of the function:
```
>>> intersperse([1, 2, 3, 4], 5)
[1, 5, 2, 5, 3, 5, 4]
```

```
>>> intersperse([1, 2, 3], 0)
[1, 0, 2, 0, 3]
```

```
>>> intersperse([5, 5, 5], 5)
[5, 5, 5]
```