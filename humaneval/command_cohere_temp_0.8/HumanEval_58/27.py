```python
def common(l1, l2):
    return sorted(set(l1).intersection(l2))
```

The `set` function is used to remove duplicate elements from both lists, and `intersection` is used to find the common elements between the two resulting sets. Finally, `sorted` is applied to order these common elements. 

This solution adheres to the problem statement and succeeds in passing the given tests. You can implement the test case by writing:
```python
>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
[1, 5, 653]
>> common([5, 3, 2, 8], [3, 2])
[2, 3]
```

These test cases correspond to the ones provided in the initial problem statement.