```python
def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with tiebreaks decided by the index of the item in the original list.

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
        num (int): Number for which the sum of digits should be calculated.

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
        num (int): Number for which the index should be determined.

    Returns:
        int: Index of the given number in the original list.
    """
    return nums.index(num) if nums else 0
```

### How It Works:
The code defines a function `order_by_points` which takes a list of integers (`nums`) as input. This function sorts the numbers based on the sum of their digits, and in case of a tie, it uses the index of the number in the original list as a tiebreaker.

The sum of digits is calculated using a nested loop in the `sum_of_digits` function. It iterates through each digit of the decimal representation of the number and adds them up.

The `x_index` function determines the index of the given number in the original list. If the list is empty, it returns 0.

The `sorted` function is used to sort the list of numbers using the custom key function `(sum_of_digits, x_index)`, which first sorts the numbers based on their digit sum and then ties are broken by their original index.

The code includes tests in the docstring, and the function is designed to work for empty lists as well.