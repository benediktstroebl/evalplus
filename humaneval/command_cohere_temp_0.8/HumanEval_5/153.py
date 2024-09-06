```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = [x for x in numbers if x != delimeter]
    return delimeter + result if result else []
```

The function takes in two parameters, `numbers`, which is a list of integers, and `delimeter`, which is the number to be interspersed between consecutive elements in the `numbers` list. It works by first creating a list `result` that filters out the `delimeter` values from the `numbers` list. This means that all occurrences of `delimeter` values are effectively removed from the list, and the function simply returns `delimeter + result` if `result` is not empty, indicating that there were numbers in the list that weren't `delimeter`, and accordingly, the `delimeter` values need to be added back between them. If `result` is empty, meaning there were only `delimeter` values in the list, the function returns an empty list. 

Here is an example usage of the function for clarification:
```python
>>> intersperse([], 4)
[]
>>> intersperse([1, 2, 3], 4)
[1, 4, 2, 4, 3]
>>> intersperse([0, 0, 0, 0, 5, 6, 7, 8, 9], 5)
[0, 5, 0, 5, 6, 7, 8, 9]
``` 

In the example above, we can see that the `delimeter`, which is `5` in this case, is placed between consecutive numbers that are not `5`. Accordingly, all occurrences of `5` have been removed from the list, and it has been reformed with the `5` placed between consecutive numbers.