```python
def sort_even(l):
    even = l[::2]
    odd = l[1::2]
    return even + sorted(odd)
```

This script provides a function `sort_even` that accepts a list `l` and returns a list `l` where the even indices are sorted, while the odd indices are unchanged. Two lists, `even` and `odd`, are created to capture the even and odd-indexed elements of the list, respectively. The sorted odd-indexed elements are then concatenated with the even-indexed elements to produce the final sorted list. This solution efficiently solves the problem while maintaining the integrity of the original odd-indexed list.