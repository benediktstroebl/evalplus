Here is a self-contained Python function that solves the problem:

```python
def rescale_to_unit(numbers: List[float]):
    # Apply a linear transform to that list,
    # such that the smallest number will become 0 and the largest will become 1
    numbers[0] = 0  # Set the smallest number to 0
    numbers[1] = 1  # Scale the second number to make it 1
    for i in range(2, len(numbers)):  # Scale the remaining numbers to make them all 1
        numbers[i] = numbers[i] / numbers[1]
    return numbers
```

This script defines a function called `rescale_to_unit`, which takes a list of numbers as input and returns a new list where each number has been rescaled to the unit [1].0 and the smallest number becomes 0. The function scales each numbers in the list to ensure that the smallest number becomes 0 and the largest becomes 1.