Here is a self-contained Python script that solves the problem of scaling a list of numbers so that the smallest value becomes 0 and the largest becomes 1, using the `rescale_to_unit` function:
```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    
    numbers = [numbers[0] / numbers[1:] + numbers[0]]
    for num in numbers[1:]:
        numbers = [num / numbers[0]] + [num]
    return numbers
```
This function takes a list of numbers and returns a new list where each number has been rescaled to have the smallest value of 0 and the largest value of 1.

The function works by first finding the smallest number in the list and the largest number in the list. Then, it adds the list of numbers by subtracting the smallest number from each number, dividing each number by the smallest number, and adding the largest number to each number. The result is that the number is scaled to the range of 0 to 1.

This is a simple and efficient way to solve the problem of scaling a list of numbers to the unit of 0 to 1.