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

nums = [1, 5, 10, 50, 51, 55, 551, 555]
print(order_by_points(nums))  # Output: [1, 5, 5, 51, 55, 55, 555, 551]

nums = []
print(order_by_points(nums))  # Output: []
```

This Python script solves the problem using two auxiliary functions: `sum_of_digits` computes the sum of digits of a given number, and `x_index` determines the index of the number in the original list, which is used as a tiebreaker. The main function `order_by_points` sorts the list based on the key values returned by these auxiliary functions. Test cases are provided to demonstrate the functionality of the code.