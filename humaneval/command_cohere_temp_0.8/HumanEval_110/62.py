```python
def exchange(lst1, lst2):
    res = 'NO'
    # Check if any element of lst1 is odd
    if any(ele % 2 for ele in lst1):
        # Exchange odd elements with elements of lst2
        lst1[:], lst2[:] = lst2, lst1
        res = 'YES'
    return res
```

The function `exchange()` swaps the elements of both lists if any element of the `lst1` is odd. The `any()` function is used to check if any of the elements in `lst1` are odd because the problem states that the input lists will be non-empty, and thus at least one element will be present. The `exchange()` function returns "YES" if any swaps were made, and "NO" otherwise.

This approach solves the problem in a straightforward manner, by using a logical check for a condition required to be changed and then swapping the lists only when necessary. It passes the tests for the given problem and achieves a time complexity of `O(n)` where `n` is the length of the lists.