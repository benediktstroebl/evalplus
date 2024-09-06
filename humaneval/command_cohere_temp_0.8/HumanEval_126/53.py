```python
def is_sorted(lst):
    # Count the unique elements and sort the list if it contains more than one unique element
    if len(set(lst)) > 1 and not lst == sorted(lst):
        return False
    # Check if the list contains duplicate elements by iterating and verifying the next element if the current element is repeated
    for i in range(1, len(lst)):
        if lst[i] == lst[i - 1] and not i == 0:
            return False
    return True
```

This approach checks if the list is sorted first by evaluating the list to be false if it has more than one unique element and is not sorted. If the list contains only one unique element, then it is considered sorted. Additionally, if there are duplicate elements, it verifies if the list is sorted by comparing the current element with the next element. If the current element is repeated, it checks if the next element is greater than the current local element, and the list is sorted, it returns true; otherwise, it returns false. 

The main advantage of using this function is its efficiency in verifying the sort of the list in a single pass since it verifies and handles both the presence of unique elements and potential duplicate elements at the same time. 

The unit tests for this function can be extracted directly from the problem statement and are provided below:
```python
# Tests
assert is_sorted([5])
assert is_sorted([1, 2, 3, 4, 5])
assert not is_sorted([1, 3, 2, 4, 5])
assert is_sorted([1, 2, 3, 4, 5, 6])
assert is_sorted([1, 2, 3, 4, 5, 6, 7])
assert not is_sorted([1, 3, 2, 4, 5, 6, 7])
assert is_sorted([1, 2, 2, 3, 3, 4])
assert not is_sorted([1, 2, 2, 2, 3, 4])
``` 
This code provides a test suite with 8 tests, each one checking a specific case and its correspondence to the expected output.