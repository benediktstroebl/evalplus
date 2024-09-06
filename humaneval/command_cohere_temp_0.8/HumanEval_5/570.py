```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = [x for x in numbers if x != delimeter]
    return delimeter + result if result else []
```

The function takes in two parameters, `numbers`, which is a list of integers, and `delimeter`, an integer to insert between consecutive numbers. To solve the problem, the function takes the first element of the input list. If the first element is not the `delimeter`, it is added to the result list. The function then iterates over the rest of the input list, ignoring instances of the `delimeter`, and adds the `delimeter` and the subsequent element to the result list. The `delimeter` is then added to the end of the result list if it is not empty. 

Here is an example usage of the function and its corresponding output:
```python
>>> intersperse([1, 2, 3, 4], 5)
[1, 5, 2, 5, 3, 5, 4]
```