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
    Calculate the sum of digits of a given number.

    Args:
        num (int): Number for which we want to calculate the sum of digits.

    Returns:
        int: Sum of digits of the given number.
    """
    sum_digits = sum(int(d) for d in str(num))
    return sum_digits

def x_index(num):
    """
    Determine the index of a number in the original list.

    Args:
        num (int): Number whose index needs to be determined.

    Returns:
        int: Index of the given number in the original list.
    """
    ind = nums.index(num)
    return ind
```

This code provides an implementation of the 'order_by_points' function, accepting a list of numbers ('nums') and sorting them hierarchically through a computed key. The key is a tuple, where the first element is the sum of digits in a number and the second element is the index of the number in the original list. Empty lists are handled gracefully, and the function returns the appropriately sorted list. 

Furthermore, auxiliary functions 'sum_digits' and 'x_index' are presented. The former computes the sum of digits in a number, while the latter finds the index of a specific number in the original list. These functions are then utilized within the 'order_by_points' function. 

This code exemplifies Python's expressive power and readability in handling complex sorting requirements.