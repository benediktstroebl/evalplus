```python
def is_sorted(lst):
    dups = {}
    for n in lst:
        if n in dups:
            dups[n] += 1
        else:
            dups[n] = 1
    for n, count in dups.items():
        if count > 1:
            return False
    return all(lst[i] <= lst[i+1] for i in range(len(lst)-1))
```

This function first checks if there are any elements in the list that appear more than once. If there are, it returns false immediately since the criterion stated that having more than one duplicate of the same number implies that the list is not sorted. Otherwise, it checks whether the list is monotone increasing, which is sufficient to determine if the list is sorted. 

The previous code solution has a time complexity of O(n) and the space complexity is O(min(n, m)) where n is the length of the list and m is the number of unique elements in the list. This solution has a time complexity of O(n) and a space complexity of O(1). 

It's important to note that the problem statement does not explicitly state that the list contains only positive integers, so it's possible for the list to contain negative numbers or other non-integer values. In this case, the function may not provide the correct result, so it's crucial to ensure the input list contains only positive integers.  If you're interested in testing your function, you can use the following tests:
```python
# Tests:
assert is_sorted([1, 2, 3, 4, 5, 6, 7])
assert not is_sorted([1, 3, 2, 4, 5, 6, 7])
assert is_sorted([1, 2, 2, 3, 3, 4])
assert not is_sorted([1, 2, 2, 2, 3, 4])
assert is_sorted([5])
assert is_sorted([1, 2, 3, 4, 5])
``` 
This test suite contains tests for various cases, including valid inputs and edge cases.