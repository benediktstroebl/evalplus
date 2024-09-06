```python
def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with tiebreaks decided by the index of the item in the original list.

    Example:
    >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    >>> order_by_points([]) == []
    """
    if not nums:
        return []

    sorted_nums = sorted(nums, key=lambda x: (sum_of_digits(x), x_index(x)))
    return sorted_nums

def sum_of_digits(num):
    """
    Calculate the sum of the digits of the given integer.
    """
    sum = 0
    num = str(num)
    for digit in num:
        sum += int(digit)
    return sum

def x_index(num):
    """
    Find the index of the given integer in the original list.
    """
    index = nums.index(num)
    return index
```

The function **order_by_points** sorts the list of numbers according to the sum of their digits, and ties are broken according to the index of the item in the original list. The functions **sum_of_digits** and **x_index** are used as key functions within the sort to compute these metrics. To solve this problem, these functions are suitably utilized in the **order_by_points** function. 

This code should be copied and pasted into a Python environment or script file and run to see the results of the **order_by_points** function with different input lists.