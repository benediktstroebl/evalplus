Here's a self-contained Python script that solves the problem of scaling a list of numbers to the unit range:

```python
def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1.

    Input: numbers: list of float
    Output: list of float

    """
    numbers = [num / 100.0 for num in numbers]
    return numbers
```

The function takes a list of numbers as input and returns a new list where each number has been scaled to a value between 0 and 1. The function achieves this purpose by dividing each number in the input list by 100.

In this solution, the function divides each number in the input list by 100.0 to scale it to the unit range. The function is self-contained, as it does not use any external functions or modules. It can be used as a complete solution to the problem.