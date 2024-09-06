Here's a self-contained Python script that solves the problem:

```python
def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1.

    : numbers[:] // convert the list into a vector
    res = numbers[:] * [1.0, -1.0]
   0
   0, 0, 5.0, 10.0] + numbers list the wrinkles by rescaling the numbers)
    return res

# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]

result = rescale_to_unit(numbers)
```

In this script, the function **rescale_to_unit** takes a list of numbers as input and returns a new list with the same numbers, but with the scaling applied.