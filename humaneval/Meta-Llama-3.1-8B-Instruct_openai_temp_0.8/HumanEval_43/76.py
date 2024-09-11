### Pairs Sum to Zero
#### Problem Description
Write a function `pairs_sum_to_zero(l)` that takes a list of integers as an input.
The function should return `True` if there are two distinct elements in the list that sum to zero, and `False` otherwise.

#### Solution
```python
def pairs_sum_to_zero(numbers):
    """
    Returns True if there are two distinct elements in the list that sum to zero, and False otherwise.

    Args:
        numbers (list): A list of integers.

    Returns:
        bool: Whether two distinct elements sum to zero.
    """
    seen = set()
    for num in numbers:
        complement = -num
        if complement in seen:
            return True
        seen.add(num)
    return False

# Test cases
def test_pairs_sum_to_zero():
    assert not pairs_sum_to_zero([1, 3, 5, 0])
    assert not pairs_sum_to_zero([1, 3, -2, 1])
    assert not pairs_sum_to_zero([1, 2, 3, 7])
    assert pairs_sum_to_zero([2, 4, -5, 3, 5, 7])
    assert not pairs_sum_to_zero([1])

test_pairs_sum_to_zero()
```
This solution uses a set `seen` to keep track of the numbers we have seen so far.
For each number, we calculate its complement and check if it is in the `seen` set.
If the complement is in the `seen` set, it means we have found two numbers that sum to zero, so we return `True`.
If we have iterate through the entire list and not found any pairs that sum to zero, we return `False`.