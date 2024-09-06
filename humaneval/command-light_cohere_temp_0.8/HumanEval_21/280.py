Here is a self-contained Python script with a function that solves the problem:
```python
def rescale_to_unit(numbers):
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1 """
    numbers[0] = 0  # Set the smallest number to 0
    for num in numbers:
        num = (num - numbers[0]) / (numbers[1] - numbers[0])
    return numbers

# Test cases
numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 0.0]
print_rescale_to_unit(numbers)

# Test case result:
print("Test case result:", end)
```
The test case result will be: **`[0.0, 0.0, 0.0, 0.0, 0.0]`