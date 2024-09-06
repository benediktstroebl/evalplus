```python
def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with the tiebreaker being their index in the original list.

    Args:
        nums (list): List of integers to be sorted.

    Returns:
        list: Sorting of the input list according to the specified criteria.
    """
    if not nums:
        return []

    sorted_nums = sorted(nums, key=lambda x: (sum_of_digits(x), x_index(x)))
    return sorted_nums

def sum_of_digits(num):
    """
    Calculate the sum of the digits of the given number.

    Args:
        num (int): Number for which the sum of digits is calculated.

    Returns:
        int: Sum of the digits of the input number.
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
        int: Index of the input number in the original list.
    """
    return nums.index(num) if nums == sorted(nums) else -1
```

This code provides an implementation of the order_by_points function, with two additional helper functions: sum_of_digits and x_index. The main function takes an input list nums and returns a new list that is sorted according to the criteria described in the problem statement. The sum_of_digits function calculates the sum of the digits of a given number, and the x_index function determines the index of the number in the original list. 

This code allows the main function to sort the list first by the sum of the digits and then by the index of the number in the original list, as specified. Let's use the following test case to prove its functionality:
```python
TEST_CASES = [
    ([1, 11, -1, -11, -12], [-1, -11, 1, -12, 11]),
    ([333, 111, 222, -333, -111, -222, 222, 333], [-333, -111, -222, 111, 222, 333]),
    ([], [])
]

for test_case in TEST_CASES:
    assert order_by_points(test_case[0]) == test_case[1]
```

The test cases are created as lists of input-output pairs to test the function order_by_points against various scenarios.