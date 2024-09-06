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
    ind = nums.index(num)
    return ind
```

This script includes three defined functions:
1. `order_by_points(nums)` takes a list of numbers as input and sorts them according to the sum of their digits, with tiebreakers being resolved by choosing numbers with lower indices in the original list.
2. `sum_digits(num)` is a helper function to compute the sum of digits of a given number.
3. `x_index(num)` is another helper function that determines the index of a specific number within the original list.

These functions work together to correctly sort the input list according to the specified criteria.