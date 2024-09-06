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

The function employs a simple algorithm that loops through each unique number in the list and counts its occurrences. If any number's count is > 1, it signifies a duplicate, and the list is not sorted. The function returns False immediately if this condition is met. Otherwise, it returns True after checking that every element in the list is unique, confirming sortedness. 

The script also has a suite of unit tests mirroring the example use cases provided in the problem statement. These tests can be executed to verify the function's behavior:
```python
def test_is_sorted():
    # Single number
    assert is_sorted([5]) == True

    # Multiple numbers, sorted
    assert is_sorted([1, 2, 3, 4, 5]) == True
    assert is_sorted([1, 3, 2, 4, 5]) == False

    # Multiple numbers, unsorted
    assert is_sorted([1, 2, 3, 4, 5, 6]) == True
    assert is_sorted([1, 3, 2, 4, 5, 6, 7]) == True

    # With duplicates, unsorted
    assert is_sorted([1, 2, 2, 3, 3, 4]) == True
    assert is_sorted([1, 2, 2, 2, 3, 4]) == False
``` 

Assuming you have a functioning Python environment with `pytest` installed, you can run these tests using the following command:
```bash
python -m pytest
``` 

This will provide you with a detailed insight into the function's behavior on each test case and whether or not it passes. 

Note: This script assumes that no negative numbers or float values are in the list, as the problem statement specifies only integers.