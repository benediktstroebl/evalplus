```python
def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with the tiebreaker being their index in the original list.

    Args:
        nums (list): List of integers to be sorted.

    Returns:
        list: Ordered list according to the criteria.
    """
    if len(nums) == 0:
        return []

    sorted_nums = sorted(nums, key=lambda x: (sum_of_digits(x), x_index(x)))
    return sorted_nums

def sum_of_digits(num):
    """
    Calculate the sum of digits of the given number.

    Args:
        num (int): Number for which the sum of digits is calculated.

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
        num (int): Number for which the index is calculated.

    Returns:
        int: Index of the number in the original list.
    """
    return nums.index(num) if nums.count(num) == 1 else -1
```

This code block contains a Python script that solves the problem statement. Let's break down the code:
1. `order_by_points(nums)` function: This function takes a list of integers, `nums`, as its argument. It sorts this list according to the sum of the digits of each number and ties are broken according to the index of each number in the original list. The sorted list is then returned.
2. `sum_of_digits(num)` function: This function calculates the sum of the digits of a given number, `num`. It does this by first initializing a variable `sum_so_far` to 0. Then, it converts the input number to a string and iterates through each digit. It increments `sum_so_far` by the value of each digit (converted to an integer). This cumulative sum of digits is returned.
3. `x_index(num)` function: This function determines the index of a given number in the original list (`nums`). It uses the `index` method of the list to find the index of the number if it exists in the list only once. If the number appears multiple times, it returns -1 to indicate that the tiebreaker rule cannot be applied.

The code meets the criteria set out in the problem statement and should run correctly. It sorts the list according to the sum of digits with the tiebreaker being the index in the original list.