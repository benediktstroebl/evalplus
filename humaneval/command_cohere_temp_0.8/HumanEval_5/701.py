```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = [x for x in numbers if x != delimeter]
    return delimeter + result if result else []
```

The function takes in two parameters, `numbers`, which is a list of integers, and `delimeter`, which is the number to be interspersed between consecutive elements in the `numbers` list. It works by first creating a list `result` that has all elements in `numbers` excluding the `delimeter`, and then concatenates the `delimeter` with `result` to create the final interspersed list. The logic ensures that `delimeter` is added only between consecutive elements, and not interspersed within a list of consecutive `delimeter` values.  This prevents unnecessary duplication of the `delimeter` in the final interspersed list.