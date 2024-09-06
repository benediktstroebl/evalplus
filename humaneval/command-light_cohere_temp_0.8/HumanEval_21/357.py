Here's the solution to the markdown code block problem:
```python
from typing import List


def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    numbers.res= sorted(numbers)
    min_val = numbers[0]
    max_val = numbers[-1]
    scaled_numbers = [num/ (max_val - min_val) + 1 for num in numbers]
    return scaled_numbers

# Test case
numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 0.0, 0]
out= [0.0, 0.0, 0.0, 0.0]
rescale_unit(numbers)
```
This function takes a list of numbers as an input and returns a new list where each element has been rescaled to the range [0, 1]. The function sorts the input list, then calculates the minimum and maximum values from the sorted list, and uses those values to scale the input list. Finally, the function multiplies each element in the input list by the ratio of the difference between the current maximum and minimum values and adds 1 to that ratio.