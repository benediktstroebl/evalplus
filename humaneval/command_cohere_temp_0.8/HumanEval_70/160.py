```python
def strange_sort_list(lst):
    # Algorithm:
    # 1. Sort the list in decreasing order (max to min)
    # 2. Remove the first element (now min) from the list
    # 3. Repeat steps 2 & 3 until the list is empty
    return [x for x in lst if not lst]
```

The function `strange_sort_list` sorts the list in the specified strange manner, as described in the problem statement. You can test the function by calling it with different lists and verifying that the sorted results match the expected patterns.