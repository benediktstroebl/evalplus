```python
def sort_third(l: list):
    """This function takes a list l and returns a list l' such that l' is identical to l in the indic that are not divisible by three, while its values at the indic that are divisible by three are equal to the values of the corresponding indic of l, but sorted."""
    return [x if x % 3 != 0 else y for x, y in zip(l, l[1:])]

#Test the function
list1 = [5, 6, 3, 4, 8, 9, 2]
print(sort_third(list1)) 
#Expected Output: [2, 6, 3, 4, 8, 9, 5]
```