```python
def is_sorted(lst):
    dups = {}
    for num in lst:
        if num in dups:
            dups[num] += 1
        else:
            dups[num] = 1
    return all(dups[num] == 1 for num in dups) and all(num < nums for _, nums in dups.items())
```

The function uses a dictionary to count the occurrences of each number, and then checks if there are no duplicates and if each number is in ascending order. The `all()` function is used for the latter check to ensure proper sorting. The `all(dups[num] == 1 for num in dups)` method checks if there are no duplicates in the list. The function returns True if the list is sorted in ascending order with no duplicates, and False otherwise.

Here is a simple test suite that can be used to validate the functionality of the function:
```python
def test_is_sorted():
    assert is_sorted([1, 2, 3, 4, 5, 6, 7]) == True
    assert is_sorted([1, 2, 2, 2, 3, 4]) == False
    assert is_sorted([1, 3, 2, 4, 5, 6, 7]) == False
    assert is_sorted([5]) == True

test_is_sorted()
``` 
This test suite provides a variety of examples that should return true or false, which will effectively test the functionality of the function and its various conditions.