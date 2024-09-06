```python
def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indic that are not divisible by three, while its values at the indic that are divisible by three are equal
    to the values of the corresponding indic of l, but sorted."""
    return [i for i in l if not(i % 3)][::3] + [i for i in l if i % 3]
```
The function sort_third takes a list l as input and returns a new list l'. It uses list comprehension and a nested loop to achieve this. The function creates two new lists: the first list contains all the values in l that are not divisible by 3 (indicating by the condition not(i%3)), and the second list contains all the values in l that are divisible by 3 (indicated by the condition i%3). 
The function then concatenates the two lists, and returns the new list l'.