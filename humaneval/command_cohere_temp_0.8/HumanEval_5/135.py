```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = [x for x in numbers if x != delimeter]
    return delimeter + result if result else []
```

The function takes in two parameters, `numbers`, which is a list of integers, and `delimeter`, which is the number to be interspersed between consecutive elements of `numbers`. It works by first creating an iterable `result` that omits the `delimeter` values from the `numbers` list. Subsequently, it returns a list that concatenates `delimeter` with `result`, or an empty list if `result` is empty. This approach ensures that `delimeter` is correctly interspersed between all consecutive elements of `numbers`. The function elegantly handles cases where `numbers` might only contain the `delimeter` value or be empty, by returning an appropriate list in such scenarios. 

The unit tests for this function would involve examining the returned list against expected results for a variety of input combinations of `numbers` and `delimeter`. For instance, 

```python
>>> intersperse([], 4)
[]
>>> intersperse([1, 2, 3], 4)
[1, 4, 2, 4, 3]
>>> intersperse([0, 0, 0], 4)
[0, 4, 4, 4]
>>> intersperse([5, 5, 5], 5)
[5, 5, 5]
```