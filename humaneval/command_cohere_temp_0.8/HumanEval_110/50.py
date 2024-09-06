```python
def exchange(lst1, lst2):
    res = 'NO'
    # Check if any element of lst1 is odd
    if any(ele % 2 for ele in lst1):
        # Check if any odd element of lst1 is in lst2
        if any(ele % 2 for ele in lst2) and all(ele % 2 == 0 for ele in lst1):
            res = 'YES'
    return res
```

The method uses two logical statements:
1. If any element of the list `lst1` is odd, then...
2. If any odd element of `lst1` is in `lst2` and all elements of `lst1` are even, then...

The first conditional statement is handled by the `any()` function combined with the `ele % 2` expression, which checks if the element is odd. The second conditional statement is handled by another `any()` function that checks if there are any odd elements in `lst2`, and the `all()` function that checks if all elements of `lst1` are even.

The script returns the appropriate response depending on the logical outcome.

This approach ensures that if any element of `lst1` is odd, the function checks whether it can be exchanged with an odd element from `lst2` to make all elements in `lst1` even. The function terminates early if any element of `lst1` is even, as it is then possible to exchange elements to make all elements in `lst1` even.