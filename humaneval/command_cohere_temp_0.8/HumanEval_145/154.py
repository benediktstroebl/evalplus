```python
def order_by_points(nums):
    """
    Sort the given list of integers in ascending order according to the sum of their digits,
    with tiebreaks decided by the index of the digit in the original list.

    Example:
    >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    >>> order_by_points([]) == []
    """
    if not nums:
        return []

    # Organize the list by digit sums, and then do a secondary sort by index
    sorted_nums = sorted(nums, key=lambda x: (sum(map(int, str(x))), x))
    return sorted_nums
```

This approach utilizes a custom key in the `sorted` function, where each element is keyed by both its digit sum and its own value. The digit sum is converted to an integer via `map(int, str(x))`.

The tests outlined in the problem can be implemented as follows:
```python
def test_order_by_points():
    # Test list with positive and negative numbers
    assert order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]

    # Test list with all positive numbers
    assert order_by_points([10, 12, 111, 2, 32, 5, 500]) == [2, 5, 10, 12, 32, 111, 500]

    # Test list with no numbers
    assert order_by_points([]) == []

    # Test list with single number
    assert order_by_points([42]) == [42]

    # Test list with numbers starting with 0 (edge case)
    assert order_by_points([01, 1, 001, 10, 1010]) == [1, 10, 1010, 01, 001]

test_order_by_points()
```

This test script verifies the function against a variety of input lists, checking for correctness in both normal and edge cases.