```python
def next_smallest(lst):
    if not lst or len(lst) < 2:
        return None
    mn, mx = min(lst), max(lst)
    sm = mn
    for v in lst:
        if v == mx:
            continue
        if v == sm:
            sm = mn
        elif v < sm:
            sm = v
    return sm
```
The algorithm for finding the second-smallest value in the list consists of the following steps:
1. Identify the minimum (`mn`) and maximum (`mx`) values in the list to narrow the search range.
2. Assume the second-smallest value is the minimum (`sm` is `mn`).
3. Iterate through the list, comparing each element to the current `sm`. 
 - If the element is equal to the maximum (`mx`), we skip it as it can't be the second-smallest.
 - If the element is equal to the current `sm`, we update `sm` to the minimum as it's not the second-smallest either.
 - If the element is smaller than the current `sm`, we update `sm` to the newer smaller value, as we've found the second-smallest. 
4. `sm` will hold the second-smallest value or `None` if there is no second-smallest element (e.g., an empty list or a list with just one element). 
Return `sm`, which stands for "second-smallest." 

This algorithm has a time complexity of O(n) since it requires iterating through the list once.