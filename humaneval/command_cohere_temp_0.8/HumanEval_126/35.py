```python
def is_sorted(lst):
    dups = {}
    for n in lst:
        if n in dups:
            dups[n] += 1
        else:
            dups[n] = 1
    return all(dups[n] == 1 for n in dups if dups[n] != 1)
```

The function employs a simple algorithm that takes advantage of Python's dictionary manipulation capabilities to detect duplicate elements in the list in O(n) time, where n is the list's length. The function then checks each element's duplicate count and returns true if every element is unique or if all the duplicates are alone. It returns false otherwise. 

Here is a simple test suite to test the function:
```python
def test_is_sorted():
    # Basic cases
    assert is_sorted([1, 2, 3, 4, 5, 6, 7])
    assert is_sorted([1, 2, 2, 3, 3, 4])
    assert not is_sorted([1, 3, 2, 4, 5, 6, 7])

    # Edge cases
    assert is_sorted([5])
    assert is_sorted([1, 2, 3, 4, 5, 6])

    # With duplicates
    assert not is_sorted([1, 2, 3, 4, 5, 6, 7, 7, 1, 2, 3])
    assert is_sorted([1, 2, 2, 3, 3, 4, 2, 3, 4, 5])

test_is_sorted()
```

This should give you a good idea of how to test the function and how it behaves under different scenarios.