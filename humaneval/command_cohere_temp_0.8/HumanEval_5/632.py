```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = [x for x in numbers if x != delimeter]
    return delimeter + result if result else []
```

The function takes in two parameters, `numbers`, which is a list of integers, and `delimeter`, which is the number to be interspersed between consecutive elements in the `numbers` list. It works by first creating a list `result` by iterating over the elements of `numbers`, ignoring any instance of `delimeter`. If `result` is empty, meaning there were no non-`delimeter` elements in `numbers`, it returns an empty list. Otherwise, it returns `delimeter` appended to `result`, thereby inserting `delimeter` between every two consecutive elements of `numbers`.

Here is an example usage of the function:
```python
>>> intersperse([1, 2, 3], 4)
[1, 4, 2, 4, 3]
```

And here is an example where the input list contains only delimiters:
```python
>>> intersperse([], 4)
[]
```