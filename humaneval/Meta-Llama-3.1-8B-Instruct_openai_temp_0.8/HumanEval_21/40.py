Here's a Python script with a function that rescales a list of numbers to the unit range (0 to 1).

```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    Args:
        numbers (List[float]): A list of numbers to be rescaled

    Returns:
        List[float]: The rescaled list of numbers
    """
    
    # Check if the list has at least two elements
    if len(numbers) < 2:
        raise ValueError("List must have at least two elements")

    # Find the minimum and maximum numbers in the list
    min_num = min(numbers)
    max_num = max(numbers)

    # Check for division by zero error
    if max_num == min_num:
        raise ValueError("All numbers in the list must be distinct")

    # Apply the linear transform
    return [(num - min_num) / (max_num - min_num) for num in numbers]

# Test the function
print(rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]))
```

This script uses a list comprehension to create a new list where each number is rescaled between 0 and 1. It does this by subtracting the minimum number from each number, then dividing by the range of the numbers (the difference between the maximum and minimum numbers). This gives a linear transformation that maps the original minimum and maximum to 0 and 1 respectively. The script also includes error checking to ensure that the input list has at least two elements and that all numbers in the list are distinct.