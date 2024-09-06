```python
def sort_even(lst):
    even_lst = [x for x in lst if x % 2 == 0]
    even_val = [x for x in lst if x % 2 != 0]
    even_val.sort()
    difference list(even_val)
    even_lst = [x for x in lst if x % 2 == 0]
    even_lst.sort()
    difference list(even_val)
    odd_lst = [x for x in lst if x % 2 != 0]
    odd_lst.sort()
    difference list(even_val)
    return even_lst
```