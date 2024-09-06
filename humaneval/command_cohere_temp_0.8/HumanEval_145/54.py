```python
def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with tiebreaks decided by the index of the item in the original list.

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
        num (int): Number whose index needs to be determined.

    Returns:
        int: Index of the given number in the original list.
    """
    ind = nums.index(num)
    return ind
```

This script includes the three functions needed to solve the problem: `order_by_points`, which sorts the list based on summations of digits and original indices; `sum_digits`, which calculates the sum of the digits of a given number; and `x_index`, which finds the index of a given number in the original list. 

The function `order_by_points` calls `sum_digits` and `x_index` as its sorting key, ensuring that the list is sorted by the desired criteria. 

To use this code, you can add it to a Python file and call `order_by_points` with a list of numbers, as demonstrated in the original problem statement. 
This solution should correctly satisfy the test cases provided.