```python
def sort_even(l: list):
    even = [x for x in l if len(x) % 2 == 0]
    odd = [x for x in l if len(x) % 2 != 0]
    return odd + sorted(even)
```

This Python script defines a function called `sort_even`, which takes a list `l` as input. It filters the list into two parts: `even`, consisting of elements with even lengths, and `odd`, consisting of elements with odd lengths. The function then returns the `odd` list in its original order, followed by a sorted version of the `even` list. This behavior is demonstrated in the example tests, where the function is applied to lists containing mixed odd and even-length elements.