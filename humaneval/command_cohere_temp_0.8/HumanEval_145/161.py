```python
def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with tiebreaks decided by the index of the integer in the original list.

    Args:
        nums (list): List of integers to be sorted.

    Returns:
        list: Ordered list according to specified criteria.
    """
    sorted_nums = sorted(nums, key=lambda x: (sum_of_digits(x), x_index(x)))
    return sorted_nums

def sum_of_digits(num):
    """
    Calculate the sum of the digits of the given number.

    Args:
        num (int): Number for which digit sum is to be calculated.

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
        num (int): Number whose index is to be determined.

    Returns:
        int: Index of the given number in the original list.
    """
    return nums.index(num) if nums else 0
```

This script defines three functions:
- The `order_by_points` function accepts a list of numbers (`nums`) and sorts them in the specified manner, returning the ordered list.
- The `sum_of_digits` function calculates the sum of the digits of a given number and returns it. 
- The `x_index` function determines the index of a given number in the original list and returns it. 

These functions work together to sort the list based on the stated criteria. Let's verify it with the original test cases:
```python
test_cases = [
    ([1, 11, -1, -11, -12], [-1, -11, 1, -12, 11]),
    ([123, 32, 456, 789, 1234, 4321], [123, 456, 789, 1234, 4321]),
    ([], []),
    (["aa", "bb", "cc", "dd", "aa", "cc", "ee", "ff", "gg", "hh"], ["aa", "aa", "bb", "cc", "cc", "dd", "ee", "ff", "gg", "hh"])
]

for test_case in test_cases:
    sorted_nums = order_by_points(test_case[0])
    assert sorted_nums == test_case[1], f"For input {test_case[0]}, the expected output is {test_case[1]}, but the actual output is {sorted_nums}"
```

The function should correctly sort the list based on the sum of digit criteria and tiebreak options when required.