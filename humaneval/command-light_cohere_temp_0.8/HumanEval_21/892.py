Here is a Python script that solves the problem of transforming a list of numbers to a unit scale:
```python
def rescale_to_unit(numbers: List[float]) -> List[float]:
    # Use slicing to copy the list of numbers
    # with the first two elements as 0 and the last two as 1.
    numbers = [numbers[0] + numbers[1:] - numbers[0] - numbers[2:]
    return numbers
```
The function `rescale_to_unit` takes a list of numbers and returns a new list with values that have been rescaled so that the smallest number is 0 and the largest is 1. This can be used as a straightforward linear transformation to a unit scale.