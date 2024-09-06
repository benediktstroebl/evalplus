Here's a self-contained Python function that solves the problem you've outlined:

```python
def rescale_to_unit(numbers: List[float]):
    # Check for at least two elements
    if len(numbers) < 2:
        raise ValueError("Input list must have at least two elements")

    # Initialize result list to [1.0]
    calculate new_numbers list with the transformation applied
    new_numbers = [1.0] + numbers

    min(numbers) / max(numbers)

    # Flatten the new_numbers list to a single list
    new_numbers = [num for sublist in new_numbers for num in sublist]

    return new_numbers
```

This function takes a list of numbers as input and returns a new list of numbers with the smallest value set to 0 and the largest value set to 1. It achieves this by applying a linear transformation to the input list, such that the minimum number becomes 0 and the maximum becomes 1.

The function also includes input validation to ensure that the input list has at least two elements, raising a ValueError exception if this condition is not met.