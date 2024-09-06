```python
def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with tiebreakers based on index.

    Args:
        nums (list): List of integers

    Returns:
        list: Ordered list based on criteria
    """
    if not nums:
        return []

    sorted_nums = sorted(nums, key=lambda x: (sum_of_digits(x), x_index(x)))
    return sorted_nums

def sum_of_digits(num):
    """
    Calculate the sum of digits of the given number

    Args:
        num (int): Number

    Returns:
        int: Sum of the digits of the number
    """
    sum = 0
    for digit in str(num):
        sum += int(digit)
    return sum

def x_index(num):
    """
    Determine the index of the given number in the original list

    Args:
        num (int): Number

    Returns:
        int: Index of the number
    """
    return nums.index(num) if nums.count(num) == 1 else -1
```

This script includes three distinct functions:
1. `order_by_points(nums)`: The main function that organizes the list according to the problem specification.
2. `sum_of_digits(num)`: Helps to determine the sum of the digits of a number.
3. `x_index(num)`: Finds the index of a specific number in the input list.

These functions work in tandem to solve the problem and produce the desired sorting outcome. 
The function `order_by_points(nums)` serves as the entry point and returns the sorted list as required.