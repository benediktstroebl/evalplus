```python
def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indic that are not divisible by three, while its values at the indic that are divisible by three are equal to the values of the corresponding indic of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    >>> sort_third([11, 22, 33, 11, 99])
    [99, 11, 33, 22, 11]
    """
    new_list = []
    for num in l:
        if num % 3 == 0:
            new_list.append(num)
   
    else:
        new_list.append(num)
        #add the new_list to l to return l'
```

This function utilizes a list comprehension to identify numbers divisible by three and appends them to the new_list. It then appends the equal to the original list to the new list of numbers that are not divisible by three.