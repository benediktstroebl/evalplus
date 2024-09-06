```python
def sort_third(lst):
    """Returns a list l' where all items are divisible by three are moved towards the beginning of the list, and all other values are ordered normally."""
    new_lst = []
    for num in lst:
        if num % 3 == 0:
            new_lst.append(num)
   
    new_lst.append(num)
   
    new_lst.sort()
   
            return new_lst
```