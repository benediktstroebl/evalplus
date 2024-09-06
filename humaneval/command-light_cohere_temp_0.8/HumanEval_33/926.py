```python
def sort_third(l: list):
    """This function takes a list l and returns a list l' such that l' is identical to l in the
    indic that are not divisible by three, while its values at the indic that are divisible by three are equal
    to the values of the corresponding indic of l, but sorted.
    Args:
        l (list): list of numbers to be sorted with special values for division by three
    Returns:
        l' (list): list of numbers, with values that are divisible by three sorted to the back, and the other values sorted normally.
    """
    Python:
    l = [1, 2, 3]
    l = sort_third(l)
    print(l)
    ```