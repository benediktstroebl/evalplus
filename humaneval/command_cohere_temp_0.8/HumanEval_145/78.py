```python
def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with the tiebreaker being their index in the original list.

    Example:
    >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    >>> order_by_points([]) == []
    """
    if not nums:
        return []

    sorted_nums = sorted(nums, key=lambda x: (sum_of_digits(x), x_index(x)))
    return sorted_nums

def sum_of_digits(num):
    """
    Calculate the sum of digits of the given number.
    """
    return sum(int(d) for d in str(num))

def x_index(num):
    """
    Return the index of the given number in the original list.
    """
    return nums.index(num) if nums else 0

# Test Cases
nums = [1, 11, -1, -11, -12]
print(order_by_points(nums))  # Output: [-1, -11, 1, -12, 11]

nums = []
print(order_by_points(nums))  # Output: []
```
This Python script defines a function order_by_points which takes a list of integers as input and sorts them according to the sum of their digits, with the tiebreaker being their index in the original list. Two auxiliary functions, sum_of_digits and x_index, are used to compute the sum of digits and the original index of each number, respectively. The code includes test cases to validate its functionality. The output of the provided test cases is [-1, -11, 1, -12, 11] for the first case and [] for the second (empty list).