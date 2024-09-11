### Median Calculation
Here's a Python function to calculate the median of a list of numbers. This function uses the built-in `sorted` function to sort the list, then checks if the list length is odd or even to determine whether to return the middle element or the average of the two middle elements.

```markdown
### Code
```python
def median(lst: list):
    """
    Return median of elements in the list lst.

    Args:
    lst (list): A list of numbers.

    Returns:
    float: The median of the list.

    Example:
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    sorted_lst = sorted(lst)
    n = len(sorted_lst)

    if n % 2 == 1:
        # If the list has an odd number of elements, return the middle element
        return sorted_lst[n // 2]
    else:
        # If the list has an even number of elements, return the average of the two middle elements
        mid1 = sorted_lst[n // 2 - 1]
        mid2 = sorted_lst[n // 2]
        return (mid1 + mid2) / 2

### Example Usage
numbers = [3, 1, 2, 4, 5]
print(median(numbers))  # Output: 3

numbers = [-10, 4, 6, 1000, 10, 20]
print(median(numbers))  # Output: 15.0
```

### Explanation
This code defines a function `median` that takes a list of numbers as input and returns the median of the list. It first sorts the list in ascending order, then checks if the list length is odd or even. If the list has an odd number of elements, it returns the middle element. If the list has an even number of elements, it returns the average of the two middle elements. The example usage demonstrates how to use the function to calculate the median of two different lists of numbers.