```python
def is_sorted(lst):
    dups = {}
    for num in lst:
        if num in dups:
            dups[num] += 1
        else:
            dups[num] = 1
    return all(dups[num] == 1 for num in dups if dups[num] != 1)
```

The function uses a simple dictionary (`dups`) to keep track of how many times each number appears in the list. If any number appears more than once and multiple times, it will set a boolean flag `False`. Otherwise, it returns `True` if the dictionary has only single occurrences of all elements, indicating that the list is sorted. 

Here is a simple test suite to ensure the function behaves correctly:
```python
def test_is_sorted():
    # Basic cases
    assert is_sorted([5])
    assert is_sorted([1, 2, 3, 4, 5])
    assert not is_sorted([1, 3, 2, 4, 5])

    # Edge cases
    assert is_sorted([1, 2, 3, 4, 5, 6])
    assert is_sorted([1, 2, 3, 4, 5, 6, 7])

    # With duplicates
    assert is_sorted([1, 2, 2, 3, 3, 4])
    assert not is_sorted([1, 2, 2, 2, 3, 4])

    # With negative numbers
    assert not is_sorted([1, -2, 3, 4, 5])
    assert not is_sorted([-2, -1, 0, 1, 2])
```