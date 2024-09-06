```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    """
    Applies a linear transformation to the input list of numbers.
    Numbers are expected to be in the form (x,y), where x is smaller than y).
    Numbers are rescaled such that smallest number in the list becomes 0 and the largest becomes 1.
    If example: [1.0,2.0,3.0, 4.0, 5]
   0, 0]
    will be transformed to:  [0.0, 0.0, 0.0, 1]
    the input list.
 ]

def test_rescale_to_unit(numbers: List[float]):
    assert rescale_to_unit(numbers) == [0.0, 0.0, 0.0, 1]
   
    assert all(x >= 0 for x in numbers)
    assert all(x <= 1 for x in numbers)
    assert sum(numbers) == len(numbers)

if __name__ == "__main__":
    numbers = [1.0, 2.0, 3.0, 4.0, 5]
   0, 0]
    test_rescale_to_unit(numbers)
```
The function `rescale_to_unit` takes a list of numbers and returns a new list where the numbers have been rescaled to form (x,y), where x is less than y). The numbers are rescaled so that the smallest number becomes 0 and the largest becomes 1. 

The function also tests to ensure that the input list is valid and that the output is as expected.