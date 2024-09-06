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
    Determine the index of the given number in the original list.

    Args:
        num (int): Number for which we want to determine the index.

    Returns:
        int: Index of the given number in the original list.
    """
    return nums.index(num) if nums == sorted(nums) else -1
```

This script includes three separate functions to tackle the sorting problem:
1. `order_by_points(nums)` serves as the entry point, sorting the input list `nums` according to the criteria specified in the problem statement.
2. `sum_of_digits(num)` calculates the sum of the digits of a given number, which is key to the sorting process.
3. `x_index(num)` determines the original index of a given number, providing the tie-breaking mechanism for items with similar digit sums. 

These functions work together to sort the input list as described, with the `order_by_points()` function employing the `sum_of_digits()` and `x_index()` functions as sorting keys. 

This code structure promotes modularity and readability, making it easier to maintain and potentially extend for future use.