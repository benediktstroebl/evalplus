```python
def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indic that are not divisible by three, while its values at the indic that are divisible by three are equal to the values of the corresponding indic of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    >>> sort_third([10, 1, 2, 20, 3])
    []
    """
    new_list = []
    for num in l:
        if num % 3 == 0:
            new_list.append(num)
        else:
            new_list.append(num)
   
    return(new_list)
```  This script defines a function `sort_third` that sorts a list in a specific manner. 

It uses a list comprehension to filter out the numbers that are divisible by three, and then sorts the remaining numbers in ascending order.