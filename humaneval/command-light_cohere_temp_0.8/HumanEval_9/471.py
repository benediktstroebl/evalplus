```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """ Returns a list of rolling maximum elements in a given list.
    def stack(iterable) --> [] 
    while not isempty(stack): 
        n = stack[-1] 
        x = stack.pop() 
        if x > n: 
            n = x
    stack.push(n) 
    return [n for i in range(len(numbers)) if not none(numbers[i]) else n]

>>> rolling_max([1, 2, 3, 2, 3])
 [3, 3, 3]
>>> rolling_max([10, 2, 3, 7, 8, 9])
 [10, 9, 8]
```