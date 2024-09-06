Here is a self-contained Python script that solves the problem of scaling down a list of numbers to a unit range:
```python
def rescale_to_unit(numbers: List[float]) -> List[float]:
    numbers = [x / 100.0 for x in numbers]
    return numbers

# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
numbers = rescale_to_unit(numbers)
```
This function takes a list of numbers and returns a new list with the same numbers but scaled to the unit range [0,1].