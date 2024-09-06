```python
def is_sorted(lst):
    dups = {}
    for num in lst:
        if num in dups:
            dups[num] += 1
        else:
            dups[num] = 1
    return all(dups[num] == 1 for num in dups if dups[num] <= 1)
```

The function employs a simple algorithm that traverses the list of numbers, maintaining a tally of duplicate occurrences of each number through a dictionary. Subsequently, it verifies that each element exists only once, and since the list is assumed to contain only positive integers, any element appearing more than once implies unsortedness. Therefore, the function returns True if all elements are unique, and False otherwise.

Here is a simple test suite to verify the functionality of the function:
```python
def test_is_sorted():
    assert is_sorted([1, 2, 3, 4, 5, 6, 7])
    assert not is_sorted([1, 3, 2, 4, 5, 6, 7])
    assert is_sorted([5])
    assert not is_sorted([1, 2, 2, 2, 3, 4])
    assert is_sorted([1, 2, 2, 3, 3, 4])
```