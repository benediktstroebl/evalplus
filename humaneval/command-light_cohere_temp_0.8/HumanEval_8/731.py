```python
from typing import List
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    return_sum=sum_product([])
        return (0,1)
    return (sum(numbers), prod(numbers))
>>>
>>> [1, 2, 3, 4]
>>> sum_product([1,2,3,4])
(4, 4)
```