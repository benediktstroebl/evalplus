```python
def sort_third(lst):
    """This function takes a list l and returns a list l' such that the list l' is sorted in such a way that
    all elements divisible by three are grouped together and are the last three elements of l'."""
    
    # Sort all numbers except 3s
    new_lst = []
    for num in lst:
        if num%3 != 0:
            new_lst.append(num)
    
    # Create a new list with the last three elements
    new_lst.append(new_lst[-3:])
    # Sort the new list
    new_lst.sort()
    micro_lst = [int(num) for num in new_lst]
    # micro_lst is now sorted
    # micro_lst = new_lst.sort()
    
    # Return a micro_lst
    lst = []
    lst.append(micro_lst)
    return lst
```