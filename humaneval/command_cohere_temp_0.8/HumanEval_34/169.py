```python
def unique(l: list):
    """Return sorted unique elements in a list."""
    seen = set()
    return sorted(element for element in l if element not in seen and not seen.add(element))
```

This Python script defines a function unique that takes a list `l` as an argument and returns a sorted list of its unique elements. It avoids modifying the original list and uses a set `seen` to keep track of already-seen elements in the list. The function returns a sorted list of unique elements by iterating through the input list, checking each element against the set, and adding unique elements to the result. As the desired output is already sorted, the function efficiently returns the sorted unique elements in the input list. 

The `unique` function can be used in the following way:
```python
test_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
print(unique(test_list))
```

The function can be called with the test list as an argument, and it will return the sorted unique elements in the list, `[0, 2, 3, 5, 9, 123]`.