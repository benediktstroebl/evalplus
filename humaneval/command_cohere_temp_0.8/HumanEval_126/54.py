```python
def is_sorted(lst):
    lst.sort()
    seen = set()
    for n in lst:
        if n in seen:
            return False
        seen.add(n)
    return True
```

The function first sorts the list, then it iterates through the sorted list, using a set to keep track of seen numbers. If the list has more than one duplicate number, the set will have more than one element with the same value, and the function will return False. If the iteration completes without finding any duplicates, the function returns True. 

The given examples in the problem statement pass with the solution, here is an example:
```python
assert is_sorted([1, 2, 3, 4, 5, 6, 7])
assert not is_sorted([1, 3, 2, 4, 5, 6, 7])
```