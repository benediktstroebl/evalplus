Here is a self-contained Python script that solves the problem of scaling a list of numbers to the unit range:
```python
def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    
    :param numbers: List[float] - List of numbers to be rescaled
    :return: List[float] - List of rescaled numbers
    """
    # Splitting the list into two lists: numbers_lower and numbers_upper
    numbers_lower = [num for num in numbers if num < 1]
    numbers_upper = [num for num in numbers if num > 1]

    # Applying the transformation: numbers_lower = [num / (num - 1)]
    numbers_upper = [num * (1 + num - 1)) for num in numbers_upper]

    return numbers_upper + numbers_lower

# Example usage:
# Test the function
numbers = [1.0, 2.0, 3.0, 4.0, 5]

rescale_to_unit(numbers)
# Print the output
print(rescale_to_unit(numbers))
```

This function takes a list of numbers and returns a new list that has been scaled to the unit range, where the smallest number is 0 and the largest number is 1. It uses a list comprehension to split the input list into two lists: numbers_lower and numbers_upper, which then have the elements of the original list that are less than or greater than 1 respectively. The function then applies the linear transformation to the numbers_upper list, which is defined as numbers_upper = [num * (1 + num - 1)) for each number num in numbers_upper. Finally, the function then returns a new list of numbers that have been rescaled to the unit range.