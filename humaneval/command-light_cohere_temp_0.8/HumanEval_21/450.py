Here is a self-contained Python script with a function that solves the problem you have provided:
```python
from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    #rescale the list
    numbers_rescale = [num / (max(numbers) - min(numbers)) for num in numbers]
    return numbers_rescale


# Example usage
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
numbers = rescale_to_unit(numbers)

print(numbers)
```
This script defines a function called `rescale_to_unit` that takes a list of numbers as input and returns a new list where each number has been scaled up to the range [0, 1]. The `max` and `min` values are calculated using the list's elements and then used to scale each number. 
The function essentially scales each number in the list so that it is between 0 and 1, with the smallest number becoming 0 and the largest number becoming 1. 
The example usage demonstrates how to use the function with a sample list of numbers.