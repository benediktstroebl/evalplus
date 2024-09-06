Here's a self-contained Python script that solves the problem:

```python
def rescale_to_unit(numbers: List[float]):
    # Apply the linear transformation to the list of numbers
    numbers = [x / 100.0 for x in numbers]
    # Return the list of numbers scaled to the unit [0,1]
    return numbers
```

This script defines a function `rescale_to_unit` that takes a list of numbers and returns a list of numbers, scaled to the unit [0,1]. The function applies the linear transformation to the list of numbers and returns the result.