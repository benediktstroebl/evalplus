Here's a solution to the problem:
```python
def rescale_to_unit(numbers):
    return [min(numbers) + x for x in range(max(numbers) - min(numbers) + 1)]
```
This function takes a list of numbers as input and applies a linear transformation to the list, such that the smallest number will become 0 and the largest will become 1. The transformed list is then returned.

To test the function, you can run the following code:
```python
numbers = [1.0, 2.0, 3.0, 4.0, 0.0]
result = rescale_to_unit(numbers)
```
This will return the result of the function, which is a list of rescaled numbers.