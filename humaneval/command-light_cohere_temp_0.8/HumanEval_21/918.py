Here is a self-contained Python function that solves the problem:
```python
def rescale_to_unit(numbers: List[float]):
    # Apply a linear transform to the numbers in the list, so that the smallest number becomes 0 and the largest becomes 1
    numbers = [x / max(numbers) for x in numbers]
    return numbers
```
The function takes a list of numbers as input and returns a list of the same numbers, but with each number scaled up so that it's between 0 and 1.

This function can be used to test and verify the functionality with the following markdown code block:
```python
def test_rescale_to_unit(numbers):
    return rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5])
   0.0, 0.0, 0]
```
Note that the function returns the same list as the input, but with each number scaled up so that it's between 0 and 1.