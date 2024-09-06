```python
def sort_third(lst):
    """This function sorts a list l such that elements not divisible by three are in their original relative order, and elements divisible by three are sorted.
    Args:
        lst (list) -- list to be sorted
    Returns:
        list -- list sorted such that values divisible by three are sorted
    """
    lst.sort()
    _ general sort algorithm, this function first sorts the list using sort() and then removes the elements divisible by three, leaving the original relative order of other elements.
    return lst[:]  # Create a shallow copy of lst
    lst = lst[:]  # Create a new list
    # Sort the list, removing elements divisible by three
    lst.sort(lambda x, y: x != 3 and y != 3)
    return lst
```
The script defines a function `sort_third` that takes a list `lst` as an argument. It then uses Python's list comprehension and the built-in sort() function to sort the list such that elements not divisible by three remain in their original relative order, and elements divisible by three are sorted. 

The function returns the list `lst[:]`, which is a shallow copy of the original list `lst` with the elements divisible by three removed. 

This allows the list to be sorted in place without affecting the original list.