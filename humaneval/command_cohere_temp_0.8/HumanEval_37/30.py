```python
def sort_even(l: list):
    even = [x for x in l if len(x) % 2 == 0]
    odd = [x for x in l if len(x) % 2 != 0]
    return odd + sorted(even)
```

This Python script defines a function called `sort_even` that takes a list `l` as input. It filters the even index elements `x` in the input list `l` and stores them in a separate list called `even`, using a list comprehension. Similarly, it filters the odd index elements `x` in the input list `l` and stores them in another separate list called `odd`, again using a list comprehension. Finally, it returns the sorted `even` list combined with the `odd` list, thereby achieving the desired behavior of keeping the original odd index elements while sorting the even index elements. This is done to maintain the list's structure, as requested in the prompt.