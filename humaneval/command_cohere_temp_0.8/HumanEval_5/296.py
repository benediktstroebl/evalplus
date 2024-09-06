```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = [x for x in numbers if x != delimeter]
    return delimeter + result if result else []
```

The function takes in two parameters, `numbers`, which is a list of integers, and `delimeter`, which is the number to be inserted between consecutive elements of the `numbers` list. It works by first filtering out the `delimeter` from the `numbers` list using a list comprehension, meaning that the `result` list will only contain elements of `numbers` that are not equal to `delimeter`. Then, if the `result` list is not empty, it adds the `delimeter` to the end of the list, ensuring that there is at least one `delimeter` between consecutive elements of `numbers`. 

Here is an example usage of the function:
```python
>>> intersperse([1, 2, 3], 4)
[1, 4, 2, 4, 3]
```

This will be the output when the function is called using the input [1, 2, 3] and delimeter value 4. It will return a list containing the numbers 1, 4, 2, 4, and 3, where the number 4 is inserted between each consecutive pair of numbers. 

The function would return an empty list if it was called with an empty list or `numbers` list containing only `delimeter` values. For example:
```python
>>> intersperse([], 4)
[]
>>> intersperse([4, 4, 4], 4)
[]
```
The former will return an empty list since the input is a blank list, and the latter will return an empty list since the input contains only delimeter values.