### Median Calculation
#### Python Script
```python
def median(nums: list):
    """
    Return median of elements in the list nums.

    Args:
        nums (list): A list of numbers.

    Returns:
        float: The median of the numbers in the list.

    Example:
        >>> median([3, 1, 2, 4, 5])
        3
        >>> median([-10, 4, 6, 1000, 10, 20])
        15.0
    """
    # Check if input list is empty
    if not nums:
        raise ValueError("Cannot calculate median of an empty list")

    # Sort the list in ascending order
    sorted_nums = sorted(nums)

    # Get the length of the list
    n = len(sorted_nums)

    # If the list has an odd number of elements, return the middle element
    if n % 2!= 0:
        return sorted_nums[n // 2]
    # If the list has an even number of elements, return the average of the two middle elements
    else:
        mid1 = sorted_nums[n // 2 - 1]
        mid2 = sorted_nums[n // 2]
        return (mid1 + mid2) / 2

# Test the function
print(median([3, 1, 2, 4, 5]))  # Output: 3
print(median([-10, 4, 6, 1000, 10, 20]))  # Output: 15.0
```
This script defines a function `median` that calculates the median of a list of numbers. It first checks if the list is empty and raises a `ValueError` in this case. Then it sorts the list in ascending order and calculates the median based on whether the list has an odd or even number of elements. The function is tested with two examples.