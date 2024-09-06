Here is a Python function that takes a list of numbers and returns a list of the same numbers rescaled such that the smallest value is 0 and the largest is 1:

```python
def rescale_to_unit(numbers):
    # Make sure the list has at least two elements
    if len(numbers) < 2:
        raise ValueError("List of numbers must have at least two elements")
    # Initialize an array to store the results
    results = []
    # Apply the linear transform
    for num in numbers:
        scaled = (num - min(numbers)) / (max(numbers) - min(numbers))
        results.append(scaled)
    return results
```

This function first checks that the list of numbers has at least two elements, and raises a ValueError if it doesn't. Then, it initializes an list to store the results of the transformation. Finally, it iterates through the list, applying the transformation by dividing each number by the difference between the largest and smallest numbers, and then adding the result to the results list.