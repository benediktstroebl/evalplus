```python
def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with tiebreakers based on their index in the original list.

    Args:
        nums (list): List of integers to be sorted.

    Returns:
        list: Ordered list based on the criteria.
    """
    if len(nums) == 0:
        return []

    sorted_nums = sorted(nums, key=lambda x: (sum_of_digits(x), x_index(x)))
    return sorted_nums

def sum_of_digits(num):
    """
    Calculate the sum of digits of the given number.

    Args:
        num (int): Number for which the digit sum is calculated.

    Returns:
        int: Sum of the digits of the number.
    """
    sum_so_far = 0
    num_str = str(num)
    for digit in num_str:
        sum_so_far += int(digit)
    return sum_so_far

def x_index(num):
    """
    Get the index of the given number in the original list.

    Args:
        num (int): Number whose index is to be determined.

    Returns:
        int: Index of the number in the original list.
    """
    return nums.index(num)
```

This code provides an implementation of the sorting function `order_by_points`, with two auxiliary functions (`sum_of_digits` and `x_index`) to help with the sorting criteria. 

The function `sum_of_digits` calculates the sum of the digits of a given number, converting it to a string and iterating through its digits to compute the sum. 

The function `x_index` determines the index of a given number in the original list, using the `index` method to find its position. 

The sorting is done using a lambda function as the key in Python's `sorted` function, with the lambda function taking the sum of digits and the index as its arguments, sorting first by the sum of digits and then by the index as a tiebreaker. 

This will produce a list that is ordered first by the sum of the digits of the numbers, and then by the index of the numbers within the original list, for numbers with equal digit sums. 
```python
def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with tiebreakers based on their index in the original list.

    Args:
        nums (list): List of integers to be sorted.

    Returns:
        list: Ordered list based on the criteria.
    """
    if len(nums) == 0:
        return []

    sorted_nums = sorted(nums, key=lambda x: (sum_of_digits(x), x_index(x)))
    return sorted_nums

def sum_of_digits(num):
    """
    Calculate the sum of digits of the given number.

    Args:
        num (int): Number for which the digit sum is calculated.

    Returns:
        int: Sum of the digits of the number.
    """
    sum_so_far = 0
    num_str = str(num)
    for digit in num_str:
        sum_so_far += int(digit)
    return sum_so_far

def x_index(num):
    """
    Get the index of the given number in the original list.

    Args:
        num (int): Number whose index is to