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

The function first sorts the list, then it iterates through the sorted list, using a set to keep track of the elements seen so far. If the set contains more than one element equal to the current element, the function returns False, indicating that the list has duplicates; otherwise, it returns True. This algorithm has a time complexity of `O(n log n)` due to the sorting step and `O(n)` for iterating the list, resulting in `O(n log n)` overall. 

Here's an example usage of the function for the first test case in the prompt:
```python
print(is_sorted([5]))
```

This should print out:
```
True
```