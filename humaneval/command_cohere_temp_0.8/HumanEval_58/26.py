```python
def common(l1, l2):
    return sorted(set(l1).intersection(l2))
```

The `set` function is used to remove duplicate elements from both lists, and `intersection` returns elements present in both adjusted lists. Finally, the result is sorted using the `sorted` function to ensure a consistent order for the output. 

This solution corresponds to the test cases provided in the problem statement, ensuring uniqueness of elements while maintaining a sorted order. Let me know if you would like me to provide further explanations on any of the steps involved in the solution!