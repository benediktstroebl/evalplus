```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    """ Returns the list of rolling max elements found until a given moment in the sequence
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4]
    """
    return [x for x, i in reversed(enumer zip(numbers, range(len(numbers)))) if i == numbers[i]]
```  This Python code defines a function `rolling_max` that calculates the list of rolling maximum elements within a given sequence of integers. The function utilizes the entered a function definition with `numbers` parameter, which is expected to be a list of integers. The function then returns a list of rolling maximum elements found until a given moment in the sequence, represented by `i` in the `enumer zip()` function. 
The `enumer zip()` function creates a tuple of the current element (`x`) and the index of the current element (`i`) in the list. The `zip()` function is then reversed to create a list of tuples in reverse order.