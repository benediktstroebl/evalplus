Here's a solution to the problem:

```python
def rescale_to_unit(numbers: List[float]):
    # Return a linear transformation that maps [0.0, 0, 0.0] to [0, 0, 1]
    return [x * (1 - 0.0) + y * (1 - 0.0) for x, y in numbers]
```

Is there anything else I can help you with?