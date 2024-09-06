```python
def common(l1, l2):
    return sorted(set(l1).intersection(l2))
```

The `common` function takes two lists as parameters and uses the `intersection` method to find the common elements between them. The `set` function is used to remove any duplicate elements from the list `l1`, and the `sorted` function is applied to return the elements in a sorted order.

This solution is concise and straightforward, and it produces the desired output for the given test cases. 

Here is an example of how to use the above code:
```python
>>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
[1, 5, 653]
>>> common([5, 3, 2, 8], [3, 2])
[2, 3]
```