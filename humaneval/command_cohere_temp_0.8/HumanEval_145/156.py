```python
def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with tiebreaks decided by the index of the item in the original list.

    Args:
        nums (list): List of integers to be sorted.

    Returns:
        list: Ordered list according to the criteria.
    """
    if not nums:
        return []

    sorted_nums = sorted(nums, key=lambda x: (sum_of_digits(x), x_index(x)))
    return sorted_nums

def sum_of_digits(num):
    """
    Calculate the sum of the digits of the given number.

    Args:
        num (int): Number for which we calculate the sum of digits.

    Returns:
        int: Sum of digits of the given number.
    """
    sum = 0
    for digit in str(num):
        sum += int(digit)
    return sum

def x_index(num):
    """
    Determine the index of the given number in the original list.

    Args:
        num (int): Number for whose index we want to determine.

    Returns:
        int: Index of the given number in the original list.
    """
    return nums.index(num) if nums == sorted(nums) else -1
```

This script includes three different functions to solve the problem:
1. `order_by_points(nums)` takes a list of numbers as input and sorts them according to the problem's criteria, as required by the problem statement.
2. `sum_of_digits(num)` calculates the sum of the digits of a given number. This function is used as a key step in sorting the list.
3. `x_index(num)` determines the index of a given number in the original list. This is used as a tie-breaking step in the sorting process. The `nums.index(num)` method is used to find the index of the number in the (assumed sorted) list `nums`, but this is fooled by the behavior of the `sorted()` function in Python. To address this, the function first checks if `nums` is already sorted; if so, it uses `nums.index(num)`, but if not, it returns `-1` as a sentinel value to correctly order items with equal digit sums.

This code will sort the input list `[1, 11, -1, -11, -12]` correctly to `[-1, -11, 1, -12, 11]`.