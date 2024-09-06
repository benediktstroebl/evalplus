```python
def sort_third(lst):
    """This function takes a list l and returns a list l' such that l' is identical to l in terms of list indices, except for values divisible by three, which are sorted to be equal to the values of their corresponding indices in l."""
    new_lst = []
    for num in lst:
        if num % 3 == 0:
            new_lst.append(num)
   
    else:
        new_lst.append(num)
        new_lst.append(num)
    new_lst.append(num)
    return new_lst
```