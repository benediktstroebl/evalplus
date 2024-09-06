Here's the solution to the problem:
```python
def rescale_to_unit(numbers: List[float]):
    # Apply a linear transform to that list, such that the smallest number will become 0 and the largest will become 1
    numbers = [num / (max(numbers) - min(numbers)) + min(numbers) for num in numbers]
    return numbers

# Tests
numbers = [1.0, 2.0, 3.0, 4.0, 5]
print(rescale_to_unit(numbers)) == [0.0, 0.0, 0.0, 1.0])
print(rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5]) == [0.0, 0.0, 0.0, 1.0])
print(rescale_to_unit([1.0, 2.0, 3.0, 4]) == [0.0, 1.0, 0])
print(rescale_to_unit([1.0, 2.0, 3.0, 4]) == [0.0, 0.0, 1])
print(rescale_to_unit([1.0, 0.0, 3]) == [0.0, 1.0, 0])
print(rescale_to_unit([1.0, 0.0, 2]) == [0.0, 1.0, 0])
print(rescale_to_unit([0.0, 0.0, 1]) == [0.0, 0])
print(rescale_to_unit([0.0, 0.0, 0]) == [0.0, 0])
print(rescale_to_unit([0.0, 0.0, 0]) == [0.0, 0])
print(rescale_to_unit([0.0, 1.0, 0]) == [0.0, 0])
print(rescale_to_unit([0.0, 1.0, 0]) == [0.0, 0])
```
The function `rescale_to_unit` takes a list of numbers as input and returns a new list where each number has been scaled to be between 0 and 1.

The test cases are a good way to verify the correctness of the function.