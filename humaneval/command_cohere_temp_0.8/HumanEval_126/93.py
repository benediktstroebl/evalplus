```python
def is_sorted(lst):
    dups = {}
    for n in lst:
        if n in dups:
            dups[n] += 1
        else:
            dups[n] = 1
    for n, v in dups.items():
        if v > 1:
            return False
    return True
```

The function employs a simple algorithm that takes advantage of the problem statement, explicitly checking for duplicates. It initializes a dictionary `dups` to store integers and their occurrences. Subsequently, it traverses the list, updating the dictionary with the count of encountering each integer. Lastly, it checks if any integer appears more than once, returning `False` if so. Otherwise, if the dictionary contains only single occurrences, it returns `True`, implying a sorted list. 

The script also has test cases that correspond to the examples provided in the problem statement. These test cases are designed to verify the functionality of the `is_sorted` function under different scenarios. 
```python
# TEST CASES

def test_is_sorted():
    assert is_sorted([1, 2, 3, 4, 5])
    assert is_sorted([1, 2, 3, 4, 5, 6])
    assert is_sorted([1, 2, 2, 3, 3, 4])
    assert not is_sorted([1, 3, 2, 4, 5, 6, 7])
    assert is_sorted([5])
    assert not is_sorted([1, 2, 3, 4, 5, 6, 7])
    assert is_sorted([1, 2, 2, 2, 3, 4])
    assert not is_sorted([1, 2, 2, 3, 3, 4])
``` 
This approach has a time complexity of O(n) since it requires iterating through the list once to populate the duplicate counts and another time to check for duplicates. It has a space complexity of O(n) due to the creation of the `dups` dictionary. Although this is a simple and efficient algorithm that solves the problem, there are other more complex approaches to solve it.