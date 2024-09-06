Here's a self-contained Python function that solves the problem of scaling down a list of numbers so that the smallest number is 0 and the largest is 1:
```python
def rescale_to_unit(numbers: List[float]) -> List[float]:
    numbers[:] = [x / max(numbers) for x in numbers]
    return numbers
```
This function takes a list of numbers as input and applies a linear transformation to each number in the list. It scales the numbers such main such small numbers to 1 and then divides the remaining numbers by the largest number to get the desired range of 0 to 1. The function then returns a list of numbers after the transformation.

The time complexity of the function is O(n), where n is the number of elements in the input list. The space complexity is O(n), as the function creates a new list of the same size.