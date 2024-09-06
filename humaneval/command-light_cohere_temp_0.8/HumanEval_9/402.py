Here's a self-contained Python function that solves the problem you described: 

```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    Generate a list of rolling maximum elements from a given list of integers.
   
    Return the
    list comprehension, a simple way to find the maximum element for each moment until a given value.
    Return a list of the maximum element for each moment.
    """ numbers: List[int] -> list of rolling_max()
    """
    return [n for n,i in enumerate(numbers) if numbers[i]>numbers[i+1]]
``` 
The function uses a list comprehension with a conditional expression to find the rolling maximum elements.