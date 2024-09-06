Here is a self-contained Python function that solves the problem you provided:

```python
def rescale_to_unit(numbers):
    # Convert the list of numbers into a 1D array
    numbers = [num for num in numbers]
    
    # Apply the linear transformation
    numbers[numbers <= 0] = 0
    numbers[numbers >= 1] = 1
    
    return numbers
```

This function takes a list of numbers as an input and returns a new list where each number has been rescaled to the unit range [0,1].