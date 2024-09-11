### Rescaling Numbers to Unit Interval

The following script defines a function `rescale_to_unit` that takes a list of numbers as input and returns a list of rescaled numbers, where the smallest number becomes 0 and the largest number becomes 1.

```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    
    Args:
        numbers (List[float]): A list of numbers to be rescaled
    
    Returns:
        List[float]: A list of rescaled numbers
    """
    
    # Check if the list contains at least two elements
    if len(numbers) < 2:
        raise ValueError("List must contain at least two elements")
    
    # Find the minimum and maximum numbers in the list
    min_num = min(numbers)
    max_num = max(numbers)
    
    # Check if all numbers are equal (i.e., the list contains a single number)
    if min_num == max_num:
        return [0.0] * len(numbers)
    
    # Apply the linear transform to rescale the numbers
    rescaled = [(num - min_num) / (max_num - min_num) for num in numbers]
    
    return rescaled

# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
rescaled_numbers = rescale_to_unit(numbers)
print(rescaled_numbers)  # [0.0, 0.25, 0.5, 0.75, 1.0]
```

This script first checks if the input list contains at least two elements. If not, it raises a `ValueError`. Then, it finds the minimum and maximum numbers in the list. If all numbers are equal, it returns a list of zeros. Otherwise, it applies the linear transform to rescale the numbers, and returns the rescaled list.

You can run this script to test the `rescale_to_unit` function with different input lists.