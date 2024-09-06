```python
def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with tiebreakers decided by the index of the item in the original list.

    Args:
        nums (list): List of integers to be sorted.

    Returns:
        list: Ordered list according to the specified criteria.
    """
    sorted_nums = sorted(nums, key=lambda x: (sum_of_digits(x), x_index(x)))
    return sorted_nums

def sum_of_digits(num):
    """
    Calculate the sum of digits of the given number.

    Args:
        num (int): Number for which we calculate the sum of digits.

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
    Determine the index of the given number in the original list.

    Args:
        num (int): Number for which we determine the index.

    Returns:
        int: Index of the given number in the original list.
    """
    return nums.index(num) if nums else 0
```

The function order_by_points takes a list of numbers as input and utilizes the sum_of_digits and x_index helper functions to sort the numbers in the desired manner. By using sum_of_digits as the primary sorting key, numbers with smaller sums of digits will appear first. As a secondary key, x_index helps break ties by ordering numbers with similar digit sums based on their original list index. This combination of keys ensures the correct sorting behavior as specified in the problem.