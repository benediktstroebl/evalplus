```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    Args:
        numbers (List[float]): A list of numbers

    Returns:
        List[float]: The rescaled list of numbers

    Example:
        >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
        [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    if len(numbers) < 2:
        raise ValueError("List must contain at least two elements")

    # Find the smallest and largest numbers in the list
    min_val = min(numbers)
    max_val = max(numbers)

    # Check for division by zero
    if max_val == min_val:
        raise ValueError("All numbers in the list are the same")

    # Apply the linear transform
    rescaled = [(num - min_val) / (max_val - min_val) for num in numbers]

    return rescaled

# Test the function
print(rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]))
```

This script defines a function `rescale_to_unit` that takes a list of numbers and returns a new list with the same values, but rescaled to the range [0, 1]. It first checks if the list has at least two elements, and if all elements are the same. If either condition is met, it raises a `ValueError`. Otherwise, it finds the smallest and largest numbers in the list, and then applies a linear transform to each number in the list, subtracting the smallest value and dividing by the range of the smallest and largest values. The result is a list of numbers in the range [0, 1]. The script then tests the function with a list of numbers.