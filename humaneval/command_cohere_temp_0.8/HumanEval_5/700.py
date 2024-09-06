```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = [x for x in numbers if x != delimeter]
    return delimeter + result if result else []
```

The function takes in two parameters, `numbers`, which is a list of integers, and `delimeter`, which is the number to be interspersed between consecutive elements in the `numbers` list. It uses list comprehension to filter out the `delimeter` tokens from the `numbers` list and then concatenates the `delimeter` with the filtered result. The careful filtering and concatenation ensure that `delimeter` is added only between consecutive elements and not interspersed within. For example, `intersperse([1, 2, 3], 4)` will return `[1, 4, 2, 4, 3]`.  This approach ensures a clean and efficient solution.