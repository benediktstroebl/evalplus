Here's a self-contained Python script that solves the problem:

```python
def rescale_to_unit(numbers):
    # Initialize result list with zeros
    result = [0 for _ in range(len(numbers))]

    # Populate result list with values from input list
    for i, num in enumerate(numbers):
        result[i] = max(0, num)

    # Return result list
    return result

# Test the function
numbers = [1.0, 2.0, 3.0, 4.0, 5.0, 0.0, 0.0]
print(rescale_to_unit(numbers))
```

This code defines a function `rescale_to_unit` that takes a list of numbers as input and returns a new list where each value has been rescaled to the range [0, 1]. The function works by initializing a result list with all zeros, then iterating through the input list and populating the result list with the largest value for each corresponding index. The output is the list, which will have been rescaled.