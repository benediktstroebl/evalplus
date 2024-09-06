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

The function first sorts the list and then checks if there are any duplicates in the list by using a set to keep track of the unique elements. If there are any duplicates, the function returns false. Otherwise, it returns true. 

This solution is efficient because it uses the built-in Python sort function, which has a worst-case time complexity of O(n log n) and a best-case time complexity of O(n log n). The loop in is_sorted also has a time complexity of O(n), which is a linear function of the number of items in the list. 

The function's space complexity is O(min(n, m)), where n is the size of the input list and m is the size of the largest duplicate set. This is because the function uses a set data structure internally to track duplicated values, which has a constant overhead. This runtime is logarithmic, which is a good balance between efficiency and simplicity. 

It is worth noting that any change to the input list (such as deleting items or adding new ones) will make the sorting algorithm react dynamically and change the active branch. Thus, the complexity remains unchanged in theory, but in practice, it may vary depending on the specific use case.