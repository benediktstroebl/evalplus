```python
def sort_even(l: list):
    even = [x for x in l if len(x) % 2 == 0]
    odd = [x for x in l if len(x) % 2 != 0]
    return odd + sorted(even)
```

This Python script defines a function called `sort_even` that takes a list `l` as an input. It filters out the elements with even lengths (i.e., those that correspond to even indices) from the input list into a separate list called `even` and then returns the original odd-length elements in the `odd` list, followed by a sorted version of the `even` list. Thus, the function sorts the even indices while keeping the odd ones intact.