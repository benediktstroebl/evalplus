```python
def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with tie breaks determined by the index of the item in the original list.

    Args:
        nums (list): List of integers to be sorted.

    Returns:
        list: Ordered list according to the specified criteria.
    """
    sorted_nums = sorted(nums, key=lambda x: (sum_digits(x), x_index(x)))
    return sorted_nums

def sum_digits(num):
    """
    Calculate the sum of digits of the given number.

    Args:
        num (int): Number for which we calculate the sum of digits.

    Returns:
        int: Sum of digits of the given number.
    """
    sum_digits = sum(map(int, str(num)))
    return sum_digits

def x_index(num):
    """
    Determine the index of the given number in the original list.

    Args:
        num (int): Number for which we determine the index.

    Returns:
        int: Index of the number in the original list.
    """
    x_index = nums.index(num)
    return x_index
```