```python
def sort_even(lst):
    even = [x for x in lst if x % 2 == 0]
    even.sort(even)
    odd = [x for x in lst if x % 2 != 0]
    odd.sort(odd)
    return even + odd
```
Do you need assistance with anything else?