Here is a self-contained Python script that solves the problem:

```python
def rescale_to_unit(numbers):
    # make sure list has at least 2 elements
    if len(numbers) < 2:
        raise ValueError("Input list must contain at least two elements")
    # create a list of tuples with the original numbers and their indices
    result = [([n, i] for i, n in enumerate(numbers)])
    # apply the transformation
    for i, j in zip(result, result[1:]):
        numbers[j[0]] = (numbers[j[0]] - numbers[j[1]]) / (numbers[j[1]] - numbers[j[0]])
    return numbers
```

This script provides a self-contained function called `rescale_to_unit` that solves the problem.  It function takes a requires a list of numbers as an argument, it first checks if the list has at least two elements, and raises a `ValueError` exception if not. Then, it creates a list of tuples that contains the original numbers and their respective indices in the list. Finally, it applies a linear transformation to the original list of numbers, where the transformation is defined by subtracting the number in the subsequent position from the number in the previous position. 

Please note that this function can be called with any list of numbers and will return a new list of numbers that has been scaled to the unit of 0 to 1.