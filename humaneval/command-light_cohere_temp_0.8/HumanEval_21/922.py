Here's the self-contained Python script that solves the problem:

```python
def rescale_to_unit(numbers: List[float]):
    """
    Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1.

    Parameters:
        numbers (List[float]): list of numbers to be rescaled

    Returns:
        List[float]: Rescaled numbers list
    """
    numbers[0] = 0  # Set the smallest number to 0
    numbers[1] = 1  # Set the largest number to 1
    for num in numbers[1:]:
        num = (num - numbers[0]) / (numbers[1] - numbers[0])
    return numbers
```

This script defines a function called `rescale_to_unit` that takes a list of numbers and returns a new list with the numbers in the range [0, 1]. The function achieves this by subtracting the smallest number from the original smallest number, dividing the result by the difference between the largest number and the original smallest number, and then adding the result to the original largest number.

Note that this script is self-contained, meaning it can be run independently and does not require any external functions or imports.