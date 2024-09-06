Here's the solution you're looking for:
```python
def rescale_to_unit(numbers: List[float]):
    # Apply a linear transform to the input list to map it to [0,1]
    return [0.5 if x < 0.0 else 1.5 if x > 0.0 else 1.25> 0.0]
> range(len(numbers) - 1)  # Use built-in slicing to avoid list mutation
```
This function takes a list of numbers as input and applies a linear transformation to that list, mapping the smallest number to 0 and the largest number to 1.

The function then returns the resulting list of rescaled numbers.