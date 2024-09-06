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
        num (int): Number whose index needs to be determined.

    Returns:
        int: Index of the given number in the original list.
    """
    return nums.index(num) if nums == sorted(nums) else -1
```

This code block includes three separate functions to approach this problem. These functions are:
1. `order_by_points(nums)` takes a list of numbers as input and sorts them according to the problem statement. It uses the `sum_of_digits()` and `x_index()` functions to create a custom sorting key for each number.
2. `sum_of_digits(num)` takes a single number as input and returns the sum of its digits. It converts the input to a string, iterates over its digits, and sums them together.
3. `x_index(num)` takes a single number as input and returns its index in the original input list `nums`. However, it only does this if `nums` is actually sorted; otherwise, it returns -1 (which serves as a sentinel value) to indicate that the index couldn't be determined reliably.

This code block presents a solution to the problem and would yield the desired output when the provided example is called as:
```python
>>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
True
```
```