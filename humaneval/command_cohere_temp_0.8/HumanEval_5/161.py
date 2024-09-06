```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = [x for x in numbers if x != delimeter]
    return delimeter + result if result else []
```

The function takes in two parameters, `numbers`, which is a list of integers, and `delimeter`, which is the number to be interspersed between consecutive elements of `numbers`. It works by first filtering out the `delimeter` from the `numbers` list using a list comprehension, thereby generating a new list `result`. If this `result` list is empty (meaning there were no elements in `numbers` that weren't `delimeter`), then the function returns an empty list. Otherwise, it returns a list that concatenates `delimeter` and the elements of `result` in alternating fashion. This means that if `result` contains even numbers of elements, then each element of `result` will be separated by `delimeter`, whereas if `result` contains an odd number of elements, then the first and last elements of `result` will have `delimeter` on either side, with `result`'s middle element being separated from its neighbors by `delimeter`.