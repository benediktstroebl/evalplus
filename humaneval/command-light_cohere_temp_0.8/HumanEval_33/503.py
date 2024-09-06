```python
def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indic that are not divisible by three, while its values at the indic that are divisible by three are equal
    to the values of the corresponding indic of l, but sorted."""
    new_l = []
    for num in l:
        if num % 3 == 0:
            new_l.append(num)
        else:
            new_l.append(num)
            new_l.append(num)
    def test_sort_third(test_list: list):
        return sorted(test_list) == [2, 6, 3, 4, 8, 9, 5]
    return test_sort_third([1, 2, 3])
```