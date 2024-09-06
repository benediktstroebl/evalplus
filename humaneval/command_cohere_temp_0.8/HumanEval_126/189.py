```python
def is_sorted(lst):
    dups = {}
    for num in lst:
        if num in dups:
            dups[num] += 1
        else:
            dups[num] = 1
    return all(dups[num] == 1 for num in dups) and all(num < nums[1] for num, nums in dups.items())
```

The function employs two conditions to evaluate the list:
1. All elements in the list occur only once, or the list contains at least two elements. This is ensured via the `all()` function and the condition `dups[num] == 1 for all num in dups`.
2. When iterating through the elements, their indices must be in ascending order. This is verified by the condition `num < nums[1] for num, nums in dups.items()`.

The function ultimately returns `True` if the list is alphabetically ordered and each element only appears once, and `False` otherwise.

A test suite for this function is as follows:
```python
def test_is_sorted():
    # Test cases from the problem statement
    assert is_sorted([5])
    assert is_sorted([1, 2, 3, 4, 5])
    assert not is_sorted([1, 3, 2, 4, 5])
    assert is_sorted([1, 2, 3, 4, 5, 6])
    assert is_sorted([1, 2, 3, 4, 5, 6, 7])
    assert not is_sorted([1, 3, 2, 4, 5, 6, 7])
    assert is_sorted([1, 2, 2, 3, 3, 4])
    assert not is_sorted([1, 2, 2, 2, 3, 4])

    # Additional test cases
    assert is_sorted([1, 2, 3, 4, 5, 4, 3, 2, 1])
    assert not is_sorted([1, 2, 3, 4, 4, 5])
    assert is_sorted([1, 1, 2, 2, 3, 3, 4, 4, 5])
    assert not is_sorted([5, 4, 3, 2, 1])
    assert is_sorted([0, 1, 2, 3, 4, 5])
    assert not is_sorted([5, 4, 3, 2, 1, 0])

test_is_sorted()
```

This test suite covers a variety of scenarios, including lists with different numbers of elements, sorted lists, and lists with duplicate elements.