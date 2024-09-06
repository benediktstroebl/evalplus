```python
def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with the tiebreaker being their index in the original list.

    Example:
        >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
        True
    """
    if not nums:
        return []

    sorted_nums = sorted(nums, key=lambda x: (sum_of_digits(x), x_index(x)))
    return sorted_nums

def sum_of_digits(num):
    """
    Calculate the sum of digits of the given integer.
    """
    sum = 0
    while num:
        sum += num % 10
        num //= 10
    return sum

def x_index(num):
    """
    Find the index of the given integer in the original list.
    """
    return nums.index(num) if num in nums else len(nums)
```

The function `order_by_points()` takes a list of numbers as input and sorts them according to the sum of their digits. If there is a tie, it breaks it based on the index of the number in the original list. Underneath the function, there are two supporting functions: `sum_of_digits()` calculates the sum of the digits of a given number, and `x_index()` finds the index of a given number in the original list. These functions are used as key parameters in the `sorted()` function to sort the input list.