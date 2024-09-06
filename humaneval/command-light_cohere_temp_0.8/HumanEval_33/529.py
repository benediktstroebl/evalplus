```python
def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indic that are not divisible by three, while its values at the indic that are divisible by three are equal to the values of the corresponding indic of l, but sorted.
    assert len(l) == 4
    assert all(x%3 == 0 for x in l) == False
    assert all(x == l[1] for x in l) == False
    assert l[0] == 2 and l[1] == 3 and l[2] == 6 and l[3] == 9
    assert l[2] == 6 and l[3] == 8 and l[4] == 9
    assert l[0] == 5 and l[1] == 6 and l[2] == 9
    assert l[3] == 8 and l[4] == 2
    l = [5, 6, 3, 4, 8, 9, 2]
    l.sort_third()
    an [2, 6, 3, 4, 8, 9, 5]
    ```