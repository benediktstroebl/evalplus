```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1.

    if numbers[0] < 0:
        numbers[:] = (-numbers[0]) / numbers[0]
        return numbers

    if numbers[-1] < 0:
        return rescale_to_unit(numbers[:-len(numbers)-1])

    return numbers

# Example
numbers = [1.5, 2.0, 3.0, 4.0, 0.5]


# Test
print(rescale_to_unit([1.5, 2, 3, 4, 0])) # [0.0, 0.0, 0.0, 0]

``` 
This Python code defines a function called `rescale_to_unit`, which transforms a list of numbers to a unit system. The function takes a list of numbers as its parameter and uses conditional statements to determine if the list should be rescaled or not. If the list contains negative numbers, the function scales the list by dividing each number by the largest negative number in the list. If the list does not contain any negative numbers, the function returns the original list. The code also includes an example of calling the `rescale_to_unit` function with a list of numbers and prints the resulting list.