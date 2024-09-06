```python
def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with tiebreaks decided by the index of the item in the original list.

    Args:
        nums (list): List of integers to be sorted.

    Returns:
        list: Sortedd list based on criteria.
    """
    if len(nums) == 0:
        return []
    sorted_ = sorted(nums, key=lambda x: (sum_of_digits(x), x_index(x)))
    return sorted_

def sum_of_digits(num):
    """
    Calculate the sum of the digits of the given number.

    Args:
        num (int): Number whose digit-sum needs to be calculated.

    Returns:
        int: Sum of the digits of the given number.
    """
    sum_ = sum(map(int, str(num)))
    return sum_

def x_index(num):
    """
    Determine the index of the given number in the original list.

    Args:
        num (int): Number whose index needs to be determined.

    Returns:
        int: Index of the given number in the original list.
    """
    index_ = nums.index(num)
    return index_
```

This script includes three key functions:
1. `order_by_points(nums)`: The main function that sorts the list of integers based on the criteria described in the problem statement. It first checks if the input list is empty, and if so, it returns an empty list. Otherwise, it uses a custom key in Python's `sorted` function to sort the numbers firstly by their digit sum and secondly by their index in the original list in case of ties.
2. `sum_of_digits(num)`: This function calculates the sum of the digits of a given number. It uses Python's `map` function to convert the integer `num` into a string and then sums up the resulting integers.
3. `x_index(num)`: This function determines the index of a given number in the original list. It uses Python's `index` function to find the index of the number in the `nums` list.