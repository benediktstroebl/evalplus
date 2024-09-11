### Rescale Numbers to Unit Interval
#### Problem Statement
Given a list of numbers, apply a linear transform to that list, such that the smallest number will become 0 and the largest will become 1.

#### Solution
```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    Args:
    numbers (List[float]): List of numbers to be rescaled

    Returns:
    List[float]: Rescaled list of numbers
    """
    # Check if the list has at least two elements
    if len(numbers) < 2:
        raise ValueError("List must have at least two elements")

    # Find the minimum and maximum values in the list
    min_value = min(numbers)
    max_value = max(numbers)

    # Check for division by zero
    if min_value == max_value:
        raise ValueError("All numbers are equal, cannot rescale")

    # Apply the linear transform
    rescaled_numbers = [(num - min_value) / (max_value - min_value) for num in numbers]

    return rescaled_numbers

# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
print(rescale_to_unit(numbers))  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
```

#### Explanation

This script defines a function `rescale_to_unit` that takes a list of numbers as input and returns the rescaled list. It first checks if the list has at least two elements, and if all numbers are equal. If either condition is met, it raises a `ValueError`. Then, it finds the minimum and maximum values in the list and applies the linear transform using a list comprehension. Finally, it returns the rescaled list. The example usage demonstrates how to use this function with a list of numbers.