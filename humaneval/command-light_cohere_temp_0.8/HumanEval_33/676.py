```python
def sort_third(l: list):
    """This function takes a list l and returns a list l' such that l' is identical to l in the 
    indicies that are not divisible by three, while its values at the indicatives that are divisible by three are 
    equal to the values of the corresponding indicatives of l, but sorted."""
    return sorted(l, key=lambda x: x[0] if x[1] % 3 == 0 else x[1] + 1)
#example
lst = [1, 2, 3]
print(sort_third(lst))
 ```