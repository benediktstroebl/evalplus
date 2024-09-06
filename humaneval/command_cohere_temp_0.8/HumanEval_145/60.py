```python
def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with the tiebreaker being their index in the original list.

    Args:
        nums (list): List of integers to be sorted.

    Returns:
        list:Sorted list according to the specified criteria.
    """
    if not nums:
        return []

    sorted_nums = sorted(nums, key=lambda x: (sum_digits(x), x_index(x)))
    return sorted_nums

def sum_digits(num):
    """
    Calculate the sum of digits of the given number.

    Args:
        num (int): Number for which we want to calculate the sum of digits.

    Returns:
        int: Sum of digits of the given number.
    """
    sum_digits = sum(int(d) for d in str(num))
    return sum_digits

def x_index(num):
    """
    Determine the index of the given number in the original list.

    Args:
        num (int): Number for whose index we want to determine.

    Returns:
        int: Index of the given number in the original list.
    """
    return nums.index(num)
```

This script includes three main components:
1. `order_by_points(nums)` function sorts the input list according to the sum of digits rule and ties breaker.
2. `sum_digits(num)` calculates the total digit sum for a given number.
3. `x_index(num)` finds the original index of a number.

These functions work together to solve the problem and provide the expected output.