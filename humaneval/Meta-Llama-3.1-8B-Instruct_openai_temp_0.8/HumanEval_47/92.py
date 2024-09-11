### Python Script to Calculate Median
```markdown
### Code
```python
def median(l: list) -> float:
    """
    Return the median of elements in the list l.

    If the length of the list is odd, the median is the middle number.
    If the length of the list is even, the median is the average of the two middle numbers.

    Args:
        l (list): A list of numbers.

    Returns:
        float: The median of the numbers in the list.
    """
    sorted_list = sorted(l)
    list_length = len(sorted_list)

    if list_length % 2 == 0:
        # If the length of the list is even, the median is the average of the two middle numbers
        median = (sorted_list[list_length // 2 - 1] + sorted_list[list_length // 2]) / 2
    else:
        # If the length of the list is odd, the median is the middle number
        median = sorted_list[list_length // 2]

    return median


### Test Cases
print("Test Case 1:")
print(median([3, 1, 2, 4, 5]))  # Expected: 3
print("\nTest Case 2:")
print(median([-10, 4, 6, 1000, 10, 20]))  # Expected: 15.0
```

### Explanation
This script defines a function `median` that takes a list of numbers as input, sorts the list, and then calculates the median based on whether the length of the list is odd or even.

### Example Use Cases
- `median([3, 1, 2, 4, 5])` returns `3`.
- `median([-10, 4, 6, 1000, 10, 20])` returns `15.0`.