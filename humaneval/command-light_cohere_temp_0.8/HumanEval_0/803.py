Here's a Python script that defines a function has_close_elements that checks if any two elements in a list are closer than a given threshold:

```python
def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold
    """
    # Sort the list ascending to make checking easier
    numbers.sort()

    list from most
    common values, closer comes first
    i = j = 0
    while i < len(numbers) - 1:
        if numbers[i] - numbers[j] <= threshold:
            return True
        j += 1
        i += 1
    return False

# Test the function
numbers = [1.0, 2.0, 3.0, 0, 8, 4, 5, 2, 0]
print(has_close_elements(numbers, 0.0))  # True, should be printed
```

The function first sorts the list of numbers and then uses two pointers, i and j, to traverse the list. If the difference between the numbers is less than or equal to the threshold, the function returns True, else it returns False.