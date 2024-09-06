Here's the solution to the markdown code block you provided:
```python
def rescale_to_unit(numbers):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1 """
    return [num / min(numbers) for num in numbers] if len(numbers) > 1 else numbers
```
This function takes a list of numbers as input and returns a new list with the numbers scaled to the unit [0, 1]. The function first checks if the list has at least two elements, then it applies the linear transformation to each number, ensuring that the smallest number becomes 0 and the largest becomes 1. 

The function then returns the new list with the scaled numbers.