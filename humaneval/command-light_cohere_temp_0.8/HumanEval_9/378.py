```python
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """
    From a given list of integers, generates a list of rolling max elements found until the given moment.
    >>> [1, 2, 3, 3, 3, 4, 4]
    """
    return [x for x,i in enumerate(zip(numbers,range(len(numbers)))) do
        i%2==0 and x<numbers[i-1]
        x>=numbers[i] and x<=numbers[i+1]
    )
```