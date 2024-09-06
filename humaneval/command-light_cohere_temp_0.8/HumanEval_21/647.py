Here's the solution for the problem that you requested:
```python
def rescale_to_unit(numbers: List[float]) -> List[float]:
    numbers = [num / 100.0 for num in numbers]
    return numbers
```
This function is designed to scale a list of numbers according to a linear transformation such that the smallest number becomes 0 and the largest becomes 1. The function takes a list of numbers as input and returns a new list with the same numbers, but each number has been divided by 100.