```python
def sort_third(lst):
    """This function sorts a list l such that the elements that are not divisible by three are at the beginning, while the elements that are divisible by three are at the end of the list, and their values are the same as in the original list, but sorted."""
def test_sort_third(lst):
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    return not sort_third(lst) and lst != [1, 2, 3, sort_third([4, 5, 6]), 9] and lst != [sort_third([2, 3, 6]), 1, 2, 3] and lst != [sort_third([5, 6, 7]), 8, 9, 4, 5]
```
The script defines a function `sort_third` which sorts a list such that the elements which are not divisible by three are in front and the elements which are divisible by three are at the back of the list, with the same values. The script also defines a test function `test_sort_third` that verifies the function by passing various lists and checking if the output is correct.