```python
def common(l1, l2):
    return sorted(set(l1).intersection(l2))
```

The `set` function is used to remove duplicate elements from both lists, and `intersection` returns elements that appear in both lists. The `sorted` function is then applied to return the elements in a consistent order. 

This solution is efficient with a time complexity of O(m + n) where m and n are the lengths of l1 and l2 respectively, since `set` and `intersection` operations take O(n) time and `sorted` takes O(m) time.

This approach ensures that the returned list contains only unique, sorted elements that appear in both lists. 

To better understand how the algorithm works, you can break down the steps like this:

1. Remove duplicates from list 1 and list 2 using the `set` function.
2. Find the intersection of the sets created from the step above.
3. Sort the resulting list. 

This method is both efficient and compatible with the spec's requirement of returning a sorted unique element list. 

This function can be used to solve the problem of finding unique common elements in two lists. Let's verify this with a test case: 

```python
def test_common():
    assert common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121]) == [1, 5, 653]
    assert common([5, 3, 2, 8], [3, 2]) == [2, 3]
```

If you would like to verify more cases, you can add additional test calls to `test_common()` to cover a variety of scenarios. 

Let me know if I can help with anything else!