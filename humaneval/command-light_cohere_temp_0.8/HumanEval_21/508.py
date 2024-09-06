Here's a self-contained Python function that solves the problem:

```python
def rescale_to_unit(numbers: List[float]):
    return [x / min(numbers) for x in numbers] if numbers else [x * (1 - min(numbers)) for x in numbers]
```

This function applies a linear transformation to the input list of numbers, such that the smallest number will become 0 and the largest will become 1. It uses the minimum value of a list to calculate the scale factor. 

You can use this function with a list of numbers and it will return a list of numbers rescaled.