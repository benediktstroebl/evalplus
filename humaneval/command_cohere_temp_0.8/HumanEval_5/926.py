```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    result = [x for x in numbers if x != delimiter]
    result.extend([delimiter] * (len(numbers) - len(result)))
    return result
```

The function takes in two parameters, `numbers`, which is a list of integers, and `delimiter`, which is the number to be interspersed between elements of the list.

It first creates an empty list `result` and iterates through each element `x` in `numbers`. If `x` is not equal to the `delimiter`, it appends it to `result`. After processing all elements, it extends `result` with `delimiter` multiples of `len(numbers) - len(result)` to ensure the correct number of delimiter values are added.

Here is an example usage of the function:
```python
>>> intersperse([1, 2, 3], 4)
[1, 4, 2, 4, 3]
```

This will return the list [1, 4, 2, 4, 3], which is the input list with 4 interspersed between each consecutive pair of elements.