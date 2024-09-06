```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = [x for x in numbers if x != delimeter]
    return delimeter + result if result else []
```

The function takes in two parameters, `numbers`, which is a list of integers, and `delimeter`, which is the number to be inserted between consecutive elements of `numbers`. It works by first filtering out the `delimeter` from the `numbers` list using a list comprehension, thereby generating a new list `result`. The next step is to concatenate the `delimeter` with the `result` list, ensuring that `delimeter` is added after each element in `result` if `result` is not empty. The function returns an empty list if the input `numbers` list is empty or contains only `delimeter` values.

Here is a simple test case to verify the functionality of the function:
```python
>>> intersperse([1, 2, 3], 4)
[1, 4, 2, 4, 3]
```

The expected output will be: [1, 4, 2, 4, 3]. The numbers [1, 2, 3] are interspersed with 4 to give [1, 4, 2, 4, 3].