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
    num_string = str(num)
    for digit in num_string:
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

This script includes three functions:
1. `order_by_points(nums)` is the main function that sorts the input list `nums` based on the sum of digits of each number and ties the break by using the index of each number in the input list.
2. `sum_of_digits(num)` calculates the sum of the digits of the given number. It converts the input number to a string, iterates over each digit, and adds them up.
3. `x_index(num)` retrieves the index of the given number in the original list. It uses `nums.index(num)` to find the position of the number in the original list.

These functions work together to sort the input list according to the specified criteria. 
```python
# Test the function
assert order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
assert order_by_points([10, 9, 20, 2, 3]) == [2, 3, 9, 10, 20]
assert order_by_points([-5, -10, -3, -8, -1]) == [-8, -10, -5, -3, -1]
assert order_by_points([]) == []
``` 
This code block includes example tests to ensure that the `order_by_points` function works correctly according to the problem statement.