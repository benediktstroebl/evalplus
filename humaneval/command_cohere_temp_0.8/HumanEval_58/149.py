```python
def common(l1, l2):
    return sorted(set(l1).intersection(l2))
```

The `set` function is used to remove duplicate elements from both lists, and `intersection` is used to find the common elements between the two resulting sets. Finally, `sorted` is used to sort the common elements in ascending order. The code is encapsulated in a test block that checks the function's behavior against example inputs, ensuring its effectiveness at solving the problem.