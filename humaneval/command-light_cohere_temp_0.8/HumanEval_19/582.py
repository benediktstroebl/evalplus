Here is a Python script that includes the function `sort_numbers` which sorts a list of numbers in ascending order:
```python
from typing import List

def sort_numbers(numbers: List[int]) -> List[str]:
    """ Input is a list of numbers, sorts them and returns as string.
    >>> sort_numbers([1,3,5])
    ['one', 'three', 'five']
    """
    numbers.sort()
    very = []
    for num in numbers:
        very = str(num)
        very.append()
   
    very.sort()
    first= True)
    return ' '.join(very)
```
This function takes a list of numbers and returns a string with the numbers sorted in ascending order.