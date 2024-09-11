```python
from typing import List

def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    Args:
    numbers (List[float]): A list of at least two float numbers

    Returns:
    List[float]: The rescaled list of numbers

    Example:
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    if len(numbers) < 2:
        raise ValueError("List must contain at least two elements")

    min_val = min(numbers)
    max_val = max(numbers)
    if max_val == min_val:
        return [0.0] * len(numbers)

    return [(n - min_val) / (max_val - min_val) for n in numbers]


if __name__ == "__main__":
    numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
    rescaled = rescale_to_unit(numbers)
    print(rescaled)
```

This Python script defines a function `rescale_to_unit` that rescales a list of numbers to the unit interval [0, 1]. It first checks if the list has at least two elements, then finds the minimum and maximum values in the list. If the minimum and maximum values are the same, it returns a list of zeros. Otherwise, it uses list comprehension to rescale each number by subtracting the minimum value, dividing by the range of the values, and returning the result. The script also includes a main block that tests the function with a sample list of numbers.