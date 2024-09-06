Here's a self-contained Python function that solves the problem:

```python
def rescale_to_unit(numbers):
    return [num / min(numbers) for num in numbers]

# Example usage
numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
rescale_to_unit(numbers)
```

The `rescale_to_unit` function takes a list of numbers as input and returns a new list with the same numbers, but each has been rescaled to the unit between 0 and 1.

The function works by creating a new list that contains the same numbers, but each with the same magnitude. The minimum value in the list is used to determine the minimum number that will become 0, and the list is then rescaled using the formula `num / min(numbers)`.