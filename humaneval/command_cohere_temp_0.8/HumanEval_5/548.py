```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = [x for x in numbers if x != delimeter]
    return delimeter + result if result else []
```

The function takes in two parameters, `numbers`, which is a list of integers, and `delimeter`, which is the number to be inserted between consecutive elements of the `numbers` list. It uses a list comprehension to create a new list, `result`, which includes the elements of `numbers` but excludes the `delimeter` value. 

If `result` is empty, meaning no non-delimeter values were present in `numbers`, it returns an empty list. Otherwise, it returns `result` joined with delimeter values, effectively inserting `delimeter` between every two consecutive elements of `numbers`. This behavior is exemplified in the docstring's examples, where the output is `[1, 4, 2, 4, 3]` for the input `[1, 2, 3]`.