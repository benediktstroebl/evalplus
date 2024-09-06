Here is a self-contained Python script with a function that solves the problem:
```python
from typing import List
def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1.
    
    Args:
        numbers (List[float]): The list of numbers to be rescaled.
    Returns:
        List[float]: The list of rescaled numbers.

    """
    numbers = [1.0, 2.0, 3.0, 4.0, 5]
   
    numbers = [0.0, 0.0, 0.0, 0.5]
    resample = numbers / (-1.0)
   5] / (1.0)  #  0.0
    def main():
        return rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5])
```

You can use this function to solve the problem and test it with different inputs.  It's a general approach to solving problems in Python, where you create a function that takes a problem as an argument and returns the solution to that problem.