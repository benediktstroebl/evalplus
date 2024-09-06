```python
def sort_third(lst):
    # get the list elements
    x = [int(i) for i in lst]
    # find the indices of elements that are divisible by three
    i = 0
    while i < len(x) and x[i] % 3 == 0:
        i += 1
    # create a new list with elements at the i indices
    y = [x[i] for i in range(len(x)) if i != i]
    # sort the new list
    z = sorted(y)
    # replace the list with the sorted list
    lst.sort = z
    string(lst)
    return lst
``` 
The above function sorts a given list lst, such that values at the indices that are divisible by three are the same, while the rest are sorted. The function uses a simple list comprehension to find the indices, then a new list with the desired values, and finally sorts the new list.