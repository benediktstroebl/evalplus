Here is a self-contained Python script that solves the problem of scaling a list of numbers according to a given range:

```python
def rescale_to_unit(numbers: List[float]):
    """
    Apply a linear transform to the list of numbers, such that the smallest number will become 0 and the largest will become 1.
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5])
   
    scale the numbers so that the smallest value will be 0 and the largest value will be 1.
    """
    list = [1.0, 2.0, 3.0, 4.0, 5]
   0]
    new_list = [x / max(numbers) for x in numbers]
    return new_list
```