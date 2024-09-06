Here's a self-contained Python function that solves the problem you mentioned:
```python
def rescale_to_unit(numbers: List[float]):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    numbers = [x / 100 for x in numbers]
    return numbers

numbers = [1.0, 2.0, 3.0, 4.0, 0.0, 0.5, 0]

print(rescale_to_unit([1.0, 2.0, 3.0, 4.0, 0)) == [0.0, 1.0, 0.0, 0])

```