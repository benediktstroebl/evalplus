```python
def common(l1, l2):
    return sorted(set(l1).intersection(l2))
```

The `set` function is used to remove duplicate elements from both lists, and `intersection` returns elements that appear in both adjusted lists. Finally, the result is sorted using the `sorted` function to ensure a consistent order for the output. 

This approach ensures that each element is included in the output only once, and the output is sorted accordingly. Let's verify the results using the provided tests:
```python
>>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
[1, 5, 653]
>>> common([5, 3, 2, 8], [3, 2])
[2, 3]
```

The output is consistent with the expected output in the problem statement. Therefore, the new response successfully solves the problem. 

If you have any more questions or need further assistance, feel free to ask!