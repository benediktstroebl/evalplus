Here's the solution you asked for:
```python
def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    :param numbers: list[float]
    :return: list[float]
    """
    numbers.res rescale(numbers)
    numbers[::-1] = (numbers / 1.0)
    def rescale(numbers: List[float]):
        """ Rescale a list of numbers to the range [0, 1].
        :param numbers: list[float]
        :return: list[float]
        """
        for i in range(len(numbers)):
            numbers[i] = (numbers[i] / max(numbers))
        return numbers[::-1]
```
This script defines a function `rescale_to_unit` that takes a list of numbers and applies a linear transformation to the list, such that the smallest number will become 0 and the largest will become 1. The `rescale` function returns the list of the original numbers with the transformation applied.