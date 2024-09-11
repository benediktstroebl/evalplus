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
        raise ValueError("The list must have at least two elements")

    # Find the minimum and maximum values in the list
    min_val = min(numbers)
    max_val = max(numbers)

    # Check if all values in the list are equal
    if min_val == max_val:
        return [0.0] * len(numbers)

    # Apply the linear transform
    rescaled = [(num - min_val) / (max_val - min_val) for num in numbers]

    return rescaled

# Example usage
print(rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]))
```

This script defines a function `rescale_to_unit` that takes a list of numbers and returns the rescaled list. The rescaled list has the smallest number from the original list as 0 and the largest number as 1. The script also includes an example usage and handles edge cases where the list has less than two elements or all values are equal. 

The linear transform is applied using a list comprehension, which makes the code efficient and easy to read. The time complexity of this script is O(n), where n is the number of elements in the input list, making it suitable for large lists.