Here's a Python script with a function that solves the specified problem using NumPy for efficient array operations:

```markdown
### rescale_to_unit Function

This function takes a list of numbers and returns a new list where the smallest number is 0 and the largest is 1.
#### Code

```python
import numpy as np
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
    # Ensure the list has at least two elements
    if len(numbers) < 2:
        raise ValueError("Input list must have at least two elements")

    # Convert the list to a NumPy array for efficient operations
    numbers_array = np.array(numbers)
    
    # Find the minimum and maximum values in the array
    min_value = np.min(numbers_array)
    max_value = np.max(numbers_array)
    
    # Check for division by zero
    if min_value == max_value:
        raise ValueError("All numbers in the list are equal")

    # Apply the linear transform to the array
    rescaled_array = (numbers_array - min_value) / (max_value - min_value)
    
    # Convert the rescaled array back to a list and return
    return rescaled_array.tolist()

# Example usage:
print(rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]))
```

#### Explanation

The function `rescale_to_unit` takes a list of numbers and returns a new list where the smallest number is 0 and the largest is 1. It uses NumPy for efficient array operations.

Here's how it works:

1.  It checks if the input list has at least two elements. If not, it raises a `ValueError`.
2.  It converts the list to a NumPy array for efficient operations.
3.  It finds the minimum and maximum values in the array.
4.  It checks if all numbers in the list are equal. If so, it raises a `ValueError`.
5.  It applies a linear transform to the array by subtracting the minimum value from each element and then dividing by the range (maximum - minimum).
6.  Finally, it converts the rescaled array back to a list and returns it.

You can use this function to rescale a list of numbers in the same way as shown in the example usage.