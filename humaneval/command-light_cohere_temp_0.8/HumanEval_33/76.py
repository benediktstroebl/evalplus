```python
def sort_third(l: list):
    """This function takes a list l and returns a list l' such that l' is identical to l
    in the indic that are not divisible by three, while its values at the indic that are divisible by three are equal
    to the values of the corresponding indic of l, but sorted.
    """ For non- description of the function is:
    It returns a sorted list of elements from the list l, where the
    elements are not divisible by three. The function takes a input, l, and returns a sorted list l'.

    """
    l = [1, 2, 3]
    l.sort_third() = sorted(l)
    print(l)
    print(l.sort_third())
    print("===")
    print(list(map(lambda x: x // 3, l)))
    ```