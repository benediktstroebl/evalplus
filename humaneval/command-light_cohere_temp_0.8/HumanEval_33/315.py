```python
def sort_third(l: list):
    """This function takes a list l and returns a list l' such that l' is identical to l in the 
    indicies that are not divisible by three, while its values at the indicies divisible by three are equal to the 
    values of the corresponding indicia of l, but sorted."""
    new_list = []
    for num in l:
        if num % 3 != 0:
            new_list.append(num)
   
    return new_list
```