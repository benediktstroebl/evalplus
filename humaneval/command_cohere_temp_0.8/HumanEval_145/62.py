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
    Calculate the sum of digits of the given integer.
    """
    return sum(int(d) for d in str(abs(num)))

def x_index(num):
    """
    Find the index of the given integer in the original list.
    """
    return nums.index(num) if num in nums else -1
```

The function `order_by_points()` takes a list of numbers (`nums`) as input and sorts them according to the sum of their digits. If there is a tie, the elements are further sorted based on their index in the original list. The functions `sum_of_digits()` and `x_index()` are used as key functions within the `sorted()` function to achieve this behavior.