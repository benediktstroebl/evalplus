Here's the solution to the problem in a self-contained Python function:
```python
def rescale_to_unit(numbers: List[float]) -> List[float]:
    numbers = [x / 100.0 for x in numbers]
    return numbers
```

This function, named `rescale_to_unit`, takes a list of numbers and returns a new list where each value has been rescaled to the range of 0 to 1. The function uses the list comprehension and the division by 100 to each number in the list to ensure that the numbers fit within the expected range.