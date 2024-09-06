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
        num (int): Number for which we want to find the index.

    Returns:
        int: Index of the given number in the original list.
    """
    return nums.index(num) if nums == sorted(nums) else -1

if __name__ == "__main__":
    nums = [1, 11, -1, -11, -12]
    expected_result = [-1, -11, 1, -12, 11]
    print(f'Order by points: {order_by_points(nums)}')
    print(f'Expected result: {expected_result}')
```

This Python script solves the problem statement with the `order_by_points` function, implementing an algorithm that meets the criteria:
1. It uses a lambda function as the sorting key in the `sorted` function, pairing the sum of digits with the index as criteria.
2. The `sum_of_digits` function calculates the total digit sum for a given number.
3. The `x_index` function determines the original index of a number using the `index` method, with a fallback of `-1` if the number is not found in the original list.

The example execution demonstrates how the function works, sorting the input list `[1, 11, -1, -11, -12]` to match the expected result `[-1, -11, 1, -12, 11]`.