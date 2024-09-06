Here is a Python script that includes a self-contained function that solves the problem:

```python
def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1.
    
    :Return a list of transformed numbers."""
    # Splitting the list into two elements, min and max
    min_num = min(numbers)
    max_num = max(numbers)
    
    # Applying the transformation to each element
    numbers_transformed = [num / (max_num - min_num) for num in numbers]
    
    # Returning the transformed list
    return numbers_transformed
```

This function, `rescale_to_unit`, takes a list of numbers as input and returns a transformed list where the smallest number is 0 and the largest is 1. It does this transformation by taking each number and dividing it by the difference between the maximum and minimum numbers. This ensures that the maximum number will be scaled down to be less than 1, and the minimum number will be scaled up to be equal to 0.