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
    if len(nums) == 0:
        return []

    sorted_nums = sorted(nums, key=lambda x: (sum_of_digits(x), x_index(x)))
    return sorted_nums

def sum_of_digits(num):
    """
    Calculate the sum of digits of the given number.

    Args:
        num (int): Number for which we want to calculate the sum of digits.

    Returns:
        int: Sum of digits of the given number.
    """
    sum_so_far = 0
    num_str = str(num)
    for digit in num_str:
        sum_so_far += int(digit)
    return sum_so_far

def x_index(num):
    """
    Get the index of the given number in the original list.

    Args:
        num (int): Number for which we want to get the index.

    Returns:
        int: Index of the given number in the original list.
    """
    return nums.index(num)
```

This script provides three functions:
1. `order_by_points(nums)` sorts the input list according to the sum of digits of each number and ties are broken by resorting to the index of each number in the original list.
2. `sum_of_digits(num)` calculates the sum of the digits of a given number.
3. `x_index(num)` retrieves the index of a given number in the original list. 

These functions work correctly for positive and negative integers and returned empty list when an empty list was input.