Here is a self-contained Python function that solves the problem:

```python
def rescale_to_unit(numbers):
    # Make sure the list has at least 2 elements
    if len(numbers) < 2:
        raise ValueError("Input list must have at least two elements")
    
    # Apply the linear transformation
    transformed_numbers = [num / min(numbers) for num in numbers]
    
    return transformed_numbers
```

This function takes a list of numbers as input and applies a linear transformation to that list, such that the smallest number will become 0 and the largest will become 1. It then returns the also makes sure that the input list has at least two elements, otherwise, it raises a ValueError exception.