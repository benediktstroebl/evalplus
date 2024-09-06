Here is a self-contained Python script that solves the problem:

```python
def rescale_to_unit(numbers: List[float]):
    # Apply a linear transform to that list, such that the smallest number will become 0 and the largest will become 1
    result = [0.0 if n < 1 else n if n < 0 else n * (-1) for n in numbers]
    return result

# Example of passing a list of numbers to the function
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
print(rescale_to_unit(numbers))
# expected output: [0.0, 0.0, 0.0, 0.0]
```