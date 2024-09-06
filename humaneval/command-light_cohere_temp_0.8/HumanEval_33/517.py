```python
def sort_third(lst):
    # Code here to sort list lst such that numbers not divisible by three are at the beginning, and numbers divisible by three are at the end.
    return [list([i for i in lst if i % 3 == 0], lst[::3], lst[1::3])
```