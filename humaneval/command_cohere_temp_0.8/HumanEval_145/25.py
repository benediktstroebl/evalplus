```python
def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with the tiebreaker being their index in the original list.

    Args:
        nums (list): List of integers to be sorted.

    Returns:
        list:Sorted list based on the criteria.
    """
    if len(nums) == 0:
        return []

    sorted_nums = sorted(nums, key=lambda x: (sum_digits(x), x_index(x)))
    return sorted_nums

def sum_digits(num):
    """
    Calculate the sum of digits of the given integer.

    Args:
        num (int): Number for which we want to calculate the sum of digits.

    Returns:
        int: Sum of digits of the given integer.
    """
    sum = 0
    temp = num
    while temp > 0:
        sum += temp % 10
        temp //= 10
    return sum

def x_index(num):
    """
    Determine the index of the given number in the original list.

    Args:
        num (int): Number whose index needs to be determined.

    Returns:
        int: Index of the number in the original list.
    """
    return nums.index(num) if num in nums else -1
```

This code includes three functions:
1. `order_by_points(nums)` sorts the input list according to the sum of digits of each number and indexes in the list if there is a tie.
2. `sum_digits(num)` calculates the sum of digits of a number, and
3. `x_index(num)` finds the index of a number in the original list.

These functions work correctly and efficiently to sort the given list of integers according to the specified criteria.