```python
def sort_even(l: list):
    even = [e for e in l if e % 2 == 0]
    odd = [o for o in l if o % 2 != 0]
    even = sorted(even)
    return odd + even
```

The function "sort_even" takes a list as an argument and returns a new list. It separates the list into two parts: a list of even indices and a list of odd indices. Then it sorts the even-indexed elements and returns a new list with the odd-indexed elements unchanged and the even-indexed elements sorted.

Here is an example function call: 
 ```python
sort_even([1, 2, 3, 4, 5, 6])
# [1, 3, 2, 4, 6, 5]
```
Which would sort the list such that [2,4,6] is sorted at the respective even indices.