```python
from typing import List

def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    # Check if len(numbers) < 2
    if len(numbers) < 2:
        raise ValueError("The list must contain at least two numbers")

    # Define the linear transformation
    numbers = [x / 100.0 for x in numbers] + [100.0 / x for x in numbers]

    # Concatenate the original list and the scaled list
    return numbers

# Example usage
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
print(rescale_to_unit(numbers))

This function takes a list of numbers and returns a new list where each number has been scaled to the range [0,1]. The example usage shows how the function works with an example list of numbers.