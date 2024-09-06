```python
def is_sorted(lst):
    lst.sort()
    seen = set()
    for v in lst:
        if v in seen:
            return False
        seen.add(v)
    return True
```

The function first sorts the list, then it iterates through the sorted list, using a set to keep track of the elements encountered, returning false immediately after detecting a second appearance of an element, and finally returning true at the end of the loop if it completes without finding a second appearance of any element. It achieves the complexity of `O(n log(n))` due to the `sort()` method and `O(n)` due to the set operations and loop, both averaging to `O(n log(n))`, which is the average for a binary search. The approach is straightforward and scalable for longer lists.