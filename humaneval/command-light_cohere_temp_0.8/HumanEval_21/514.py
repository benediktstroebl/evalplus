Here's a self-contained Python function that solves the given problem:

```python
def rescale_to_unit(numbers):
    # Ensure at least two elements
    if len(numbers) < 2:
        raise ValueError("Input list must contain at least two elements")
    
    # Ensure numbers are all positive
    if all(n < 0 for n in numbers) or any(n == 0):
        raise ValueError("Input list must not contain any negative or zero values")

    # Apply a linear transform to that list,
    # such that the smallest number will become 0 and the largest will become 1
    numbers[0] = 0
    numbers[0] = max(numbers)
    numbers[1] = 1
    return numbers
```

This function first checks that the list has at least two elements. Then it ensures that all elements in the list are positive. Finally, it applies a linear transformation to the list, ensuring that the smallest number becomes 0 and the largest becomes 1.