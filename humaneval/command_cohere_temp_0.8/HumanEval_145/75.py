```python
def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with tiebreaks decided by the index of the item in the original list.

    >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    >>> order_by_points([]) == []
    """
    sorted_nums = sorted(nums, key=lambda x: (sum(map(int, str(x))), nums.index(x)))
    return sorted_nums
```

The function `order_by_points` sorts the list of integers `nums` by the sum of the digits of each integer in ascending order while using the index of the integer in the original list as a tiebreaker. The key argument of the `sorted` function is used to specify a custom function that computes a key value for each element before sorting. In this case, the key function takes each integer in the input list, converts it to a string, sums the integer values of each digit of the string, and returns this sum, coupled with the index of the integer in the input list, as a tuple. The sum of the digits is used for sorting, while the index is used as a tiebreaker in case two elements have the same digit sum. The returned sorted list is then returned by the function.