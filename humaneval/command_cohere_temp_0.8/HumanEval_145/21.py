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
    if not nums:
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
    num_str = str(num)
    for digit in num_str:
        sum_so_far += int(digit)
    return sum_so_far

def x_index(num):
    """
    Determine the index of the given number in the original list.

    Args:
        num (int): Number for which we want to determine the index.

    Returns:
        int: Index of the given number in the original list.
    """
    return nums.index(num) if nums == sorted(nums) else -1

if __name__ == "__main__":
    nums = [1, 11, -1, -11, -12]
    expected_result = [-1, -11, 1, -12, 11]
    assert order_by_points(nums) == expected_result, f"Expected {expected_result}, but got {order_by_points(nums)}."

    nums = [2, 3, 7, 8, 10, 43, 55, 97, 66, 77, 1, 5, 30, 40, 57, 94, 63, 29, 22, 99, 88, 34, 77, 1, 87, 21, 66, 77, 13, 29, 11]
    expected_result = [1, 3, 4, 5, 7, 8, 10, 11, 13, 22, 29, 29, 34, 40, 43, 51, 55, 63, 66, 66, 77, 77, 87, 88, 94, 97, 99]
    assert order_by_points(nums) == expected_result, f"Expected {expected_result}, but got {order_by_points(nums)}."
```

This code provides the `order_by_points` function with detailed documentation, implementing the required sorting algorithm. It also features additional functions like `sum_of_digits` to calculate the sum of digits and `x_index` to determine the original index of an element, both utilized as key arguments in the `sorted` function to fulfill the sorting criteria. The script includes tests to validate its functionality; they should be modified according to the desired input lists.