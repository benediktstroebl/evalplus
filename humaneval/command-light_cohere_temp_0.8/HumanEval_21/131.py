Here is a Python script that contains a self-contained function that solves the problem:

```python
def rescale_to_unit(numbers):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1

    :param numbers: list of floats
    :return: list of floats with values scaled to [0, 1] range
    """
    numbers_copy = numbers[:]
    numbers_copy[0] = 0
    numbers_copy[0] = (numbers_copy[0] / (max(numbers_copy) - min(numbers_copy)))
    numbers_copy[1] = 1
    return numbers_copy
```

This script defines a function called `rescale_to_unit` that takes a list of numbers and returns a list of numbers with values scaled to the range [0, 1]. The function works by first creating a copy of the input list, then dividing the first element by the range difference between the smallest and the largest elements in the list to ensure the number is scaled to zero. After that, the second element is set to one, indicating that all the numbers in the list are now scaled to the range [0, 1].