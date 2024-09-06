Here is a self-contained Python function that solves the problem of rescaling a list of numbers so that the smallest value becomes 0 and the largest becomes 1:
```python
def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1.

    : Python
    previous_numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
   0, 0.0, 0.0, 0]
    result_list = [0.0, 0.5, 0]
   0]
    return previous_numbers
}
```
This function works by creating a new list with the same number of elements as the input list, but with the smallest number in the new list set to 0 and the largest number in the new list set to 1.

The function then returns the new list, which has the same shape and content as the input list but with the smallest number replaced by 0 and the largest number replaced by 1.