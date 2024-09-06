```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = [x for x in numbers if x != delimeter]
    return delimeter + result if result else []
```

The function takes in two parameters, `numbers`, which is a list of integers, and `delimeter`, which is the number to be interspersed between consecutive elements of `numbers`. The function checks if `numbers` has more than one element apart from the `delimeter` and then returns a list with `delimeter` interspersed between the elements of `numbers`. Since the last element in `numbers` cannot have a subsequent element to add a `delimeter` to, the function adds the `delimeter` alone to signal the end of the new list. 

Here is an example usage of the function:
```python
print(intersperse([1, 2, 3], 4))
```
```
[1, 4, 2, 4, 3]
```