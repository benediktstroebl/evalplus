```python
def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with the tiebreaker being their index in the original list.

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
    num_str = str(num)
    for digit in num_str:
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

This code provides an implementation of the order_by_points function, with two additional helper functions: sum_of_digits and x_index. Here's a brief explanation of each component:
1. `order_by_points` function: This function takes a list of integers, `nums`, and sorts them in the specified order. It uses a custom key in the `sorted` function to first sort the numbers based on the sum of their digits, and then as a tiebreaker, it sorts them based on their index in the original list. The sorted list is then returned.
2. `sum_of_digits` function: This function calculates the sum of the digits of a given number, `num`. It converts the number to a string, iterates over each digit, and adds them up. This sum is then returned.
3. `x_index` function: This function determines the index of a given number in the original list (`nums`). It uses the `index` method of the list to find the index of the number if it's in the list. If the list is empty, it returns 0 as a default value.

The code includes a docstring for the top-level function, as well as inline documentation for each helper function. This summarizes the purpose and functionality of each element in the code.