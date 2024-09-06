Here's a Python script with a self-contained function that solves the problem:
```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given a list of numbers (at least two elements), apply a linear transform to that list,
        such that the smallest number will become 0 and the largest will become 1 """

    # ensure the list has at least two elements
    if len(numbers) < 2:
        raise ValueError("Input list must have at least two elements")

    # sort the list and get the two elements corresponding to the smallest and largest values
    numbers.sort()
    lowest_value = numbers[0]
    highest_value = numbers[-1]
    
    # apply linear transform using the formula x * 0.5 * (1 + (b-a)/(x-a)) where:
    # x is the current value in the list
    # a is the smallest value
    # b is the largest value
    # to normalize the list such that smallest becomes 0 and largest becomes 1
    return [lowest_value + (x - lowest_value) * 0.5 * (1.0 + (highest_value - lowest_value) / (x - lowest_value)) for x in numbers]

# Tests:
assert rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]) == [0.0, 0.25, 0.5, 0.75, 1.0]

# Edge case where input list has only two elements
assert rescale_to_unit([1.0, 3.0]) == [0.0, 0.5]

# Edge case where input list has only two elements, but in reverse order
assert rescale_to_unit([3.0, 1.0]) == [0.0, 0.5]

# Edge case where list has only one element
assert rescale_to_unit([6.0]) == [0.0]
```