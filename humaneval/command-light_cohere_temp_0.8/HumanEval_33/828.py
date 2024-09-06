```python
def sort_third(lst):
    """Returns a list l' such that l' is identical to l in the indic that are not divisible by three, while its values at the indic that are divisible by three are equal to the values of the corresponding indic of l, but sorted."""
    # input
    lst = [1, 2, 3]
    # get the index of all numbers in the list that are divisible by three
    idx = []
    for i in range(len(lst)):
        if lst[i] % 3 == 0:
            idx.append(i)
   
    # create a new list that contains the values of lst that are not divisible by three
    new_lst = []
    for i in range(len(lst)):
        if i not in idx:
            new_lst.append(lst[i])
    # sort the new list in ascending order
    new_lst.sort()
    use(lst)
    # create a new list that contains the values of lst that are divisible by three
    new_lst_divisible = []
    for i in range(len(lst)):
        if lst[i] % 3 == 0:
            new_lst_divisible.append(lst[i])
    # sort the new list in ascending order
    new_lst_divisible.sort()
   + lst
    new_lst_divisible + new_lst
    # return the new list that contains all values in lst
    return new_lst_divisible + new_lst_lst
```