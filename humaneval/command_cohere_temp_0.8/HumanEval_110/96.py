```python
def exchange(lst1, lst2):
    res = 'NO'
    even_idxs = [i for i, x in enumerate(lst1) if x % 2 == 0]
    if len(even_idxs) > 0:
        for idx in even_idxs:
            lst1[idx], lst2[idx] = lst2[idx], lst1[idx]
        res = 'YES'
    return res
```

The problem asks whether it's possible to exchange elements between two lists to make the first list consist of even numbers only. The goal is to return "YES" if this is possible and "NO" otherwise. The self-contained function `exchange` takes two lists (`lst1` and `lst2`) as input and returns a string ("YES" or "NO") as described in the specification.

This is how the function works:
1. It starts with setting the response variable `res` to 'NO' - this is the default response if no even numbers are found in `lst1`.
2. It creates a list, `even_idxs`, which contains the indices of all even numbers in `lst1`.
3. If `even_idxs` is not empty, the function iterates over each index in `even_idxs`, and swaps the corresponding elements of `lst1` and `lst2`.
4. After the swap operation, `res` is set to 'YES'.
5. Finally, the function returns the value of `res`.