```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    Args:
        numbers (List[float]): A list of numbers.

    Returns:
        List[float]: The rescaled list of numbers.

    Raises:
        ValueError: If the input list has less than two elements.

    Example:
        >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
        [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    if len(numbers) < 2:
        raise ValueError("Input list must have at least two elements.")

    min_val = min(numbers)
    max_val = max(numbers)

    if max_val == min_val:
        return [0.0] * len(numbers)

    return [(n - min_val) / (max_val - min_val) for n in numbers]

# Test the function
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
print(rescale_to_unit(numbers))  # Output: [0.0, 0.25, 0.5, 0.75, 1.0]
```

In this script, the function `rescale_to_unit` takes a list of numbers as input and returns a new list where each number has been scaled to the range [0, 1]. The smallest number in the input list is mapped to 0 and the largest number is mapped to 1.

If the input list has less than two elements, a `ValueError` is raised because it's impossible to rescale a list with less than two elements.

The function uses list comprehension to create a new list with the rescaled numbers. The rescaling is done using the formula `(n - min_val) / (max_val - min_val)`, where `n` is the current number and `min_val` and `max_val` are the smallest and largest numbers in the input list, respectively.

Finally, the script includes a test case to demonstrate the function's behavior.