```python
def sort_third(l: list):
    """This function takes a list l and returns a list l' such that l' is identical to l in the indic that are not divisible by three, while its values at the indic that are divisible by three are equal to the values of the corresponding indic of l, but sorted.
   >>>
    list(set(l) & set([3])))
    l = [1, 2, 3, 5, 6, 9]
    l.sort_third() == [ [1, 2, 3, 6, 9]
    ```