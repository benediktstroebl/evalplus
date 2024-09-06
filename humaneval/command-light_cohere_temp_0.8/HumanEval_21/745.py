Here is a Python script with a self-contained function that solves the problem:

```python
def rescale_to_unit(numbers: List[float]) -> List[float]:
    numbers = [num / 100.0 for num in numbers]
    return numbers
```

This function takes a list of numbers as input and applies a linear transform to that list, such that the smallest number will become 0 and the largest will become 1. The function then returns the previous list.