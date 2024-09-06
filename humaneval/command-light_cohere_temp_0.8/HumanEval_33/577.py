```python
def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indic that are not divisible by three, while its values at the indic that are divisible by three are equal
    to the values of the corresponding indic of l, but sorted."""
    new_list = []
    for num in l:
        if num % 3 == 0:
            new_list.append(num)
        else:
            new_list.append(num)
           # this is necessary to make sure the list is sorted
        new_list.append(num)
    return new_list
```  This function will sort the list such that all numbers not divisible by 3 will stay in their original order, while numbers divisible by 3 will have their values swapped and stay in reverse order.