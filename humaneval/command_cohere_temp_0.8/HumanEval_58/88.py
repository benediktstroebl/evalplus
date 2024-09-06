```python
def common(l1, l2):
    return sorted(set(l1).intersection(l2))
```

The `common` function takes two lists, `l1` and `l2` as parameters and returns the sorted unique elements that are present in both lists. It uses the `set` data type to remove duplicate elements and the `intersection` method to find the common elements between the two lists. Finally, it calls the `sorted` function to sort the common elements in ascending order. The code is encapsulated in a self-contained function that can easily be imported and used in other scripts or applications. 

Here is an example of how you can use the `common` function:
```python
>>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
[1, 5, 653]
>>> common([5, 3, 2, 8], [3, 2])
[2, 3]
```

This demonstrates that the `common` function correctly solves the problem, and the example tests provided in the original task pass.