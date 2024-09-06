```python
def sort_even(l: list):
    """Sorts a list l into a list l' such that l' contains the same elements as l, but with values of even indices sorted.

    Parameters:
        l (list): list of numbers, with potentially odd indices

    Returns:
        l' (list): list of numbers with even indices sorted
    """
    l = [1, 2, 3]
    l.sort_even(l)
    print(f"After sorting, list is: {l}")
    ```