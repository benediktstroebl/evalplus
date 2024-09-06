```python
def common(l1, l2):
    return sorted(set(l1).intersection(l2))
```

The `set` function is used to remove duplicate elements from both lists, and `intersection` retrieves the common elements between the two lists. Finally, `sorted` is applied to organize the result in a sorted manner. The code ensures that each element in the resulting list is unique, and the order is sorted. Furthermore, it handles various scenarios, including cases where the lists have different lengths, and when one list has elements that are not in the other.