```python
def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indic, while its values at the even indicies are equal to the values of the even indic of l, but sorted.
    """
    def get_even(lst):
        even = []
        for num in lst:
            if num%2 == 0:
                even.append(num)
        return even
    lst = [1, 2, 3]
    even = get_even(lst)
    lst = even + [3]
    l = []
    for num in lst:
        l.append(num)
    return l
```