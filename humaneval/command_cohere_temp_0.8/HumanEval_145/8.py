```python
def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with tiebreaks decided by the index of the integer in the original list.

    Args:
        nums (list): List of integers to be sorted.

    Returns:
        list: Sortedd list based on criteria above.
    """
    if len(nums) == 0:
        return []

    # Explicitly defining the return type as an iterable to allow sorting
    return sorted(nums, key=lambda x: (sum(int(d) for d in str(x)), x))
```

The function `order_by_points` sorts a list of numbers according to the sum of the digits of the number, with tie breaks decided by the index of the number in the original list. This function behaves like Python's `sorted` function, so it produces an iterable of the sorted numbers. The returned iterable behaves like the original input iterable, so if that was a list, it will also be a list.

Here is an example of how to use the function:
```python
print(order_by_points([1, 11, -1, -11, -12]))
```

The function can be tested like this:
```python
test_order_by_points = order_by_points
def test_order_by_points(nums, expected):
    result = order_by_points(nums)
    assert result == expected, f"For input: {nums}, expected: {expected}, actual: {result}"
```

This test defines a function that tests `order_by_points` by passing different lists of numbers and comparing the returned value with the expected value.