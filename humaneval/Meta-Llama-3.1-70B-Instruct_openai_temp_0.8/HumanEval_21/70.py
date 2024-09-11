```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Applies a linear transformation to a list of numbers such that the smallest number becomes 0 and the largest becomes 1.

    Args:
    numbers (List[float]): A list of floating point numbers with at least two elements.

    Returns:
    List[float]: The rescaled list of numbers.
    """
    
    # Check if the list has at least two elements
    if len(numbers) < 2:
        raise ValueError("The input list must have at least two elements.")

    # Find the minimum and maximum values in the list
    min_value = min(numbers)
    max_value = max(numbers)

    # Check if all numbers are the same to avoid division by zero
    if min_value == max_value:
        return [0.0] * len(numbers)

    # Apply the linear transformation to each number in the list
    rescaled_numbers = [(num - min_value) / (max_value - min_value) for num in numbers]
    
    return rescaled_numbers


# Example usage
if __name__ == "__main__":
    numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
    rescaled = rescale_to_unit(numbers)
    print(rescaled)  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
```