```python
def is_sorted(lst):
    dups = {}
    for num in lst:
        if num in dups:
            dups[num] += 1
        else:
            dups[num] = 1
    for num, count in dups.items():
        if count > 1:
            return False
    return all(lst[i] <= lst[i+1] for i in range(len(lst)-1))
```

The function uses a simple algorithm that checks if there are any duplicates in the list and then checks if the list is sorted. The function returns True if the list is sorted and does not contain any duplicates, and False otherwise. To showcase the functionality, here are some test cases that can be added:
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
    assert is_sorted([0, 1, 2, 3, 4, 5])  # No negative numbers
    assert is_sorted([0, 0, 0, 1, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5])  # Multiple duplicates
    assert not is_sorted([5, 4, 3, 2, 1])  # Reverse order
    assert is_sorted([0, 0, 0, 1, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9])  # Larger list
    assert not is_sorted([5, 4, 3, 2, 1, 9])  # Out of order with gap
    assert not is_sorted([4, 4, 3, 2, 1, 9])  # Duplicate integers
    assert not is_sorted([4, 5, 3, 2, 1, 9])  # Mixed integers and doubles
```

To run the tests, a simple driver function can be added to execute them:
```python
# Driver code
test_is_sorted()
``` 
The complete Python script should look as follows:
```python
def is_sorted(lst):
    dups = {}
    for num in lst:
        if num in dups:
            dups[num] += 1
        else:
            dups[num] = 1
    for num, count in dups.items():
        if count > 1:
            return False
    return all(lst[i] <= lst[i+1] for i in range(len(lst)-1))

def test_is_sorted():
    # Test cases from the problem statement
    assert is_sorted([5])
    assert is_sorted([1, 2, 3, 4, 5])
    assert not is_sorted([1, 3, 2, 4, 5])
    assert is_sorted([1, 2, 3, 4, 5, 6])
    assert is_sorted([1, 2, 3, 4, 5, 6,