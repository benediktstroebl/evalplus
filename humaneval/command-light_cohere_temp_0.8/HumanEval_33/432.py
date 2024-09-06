```python
def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the index that are not divisible by three, while its values at the index that are divisible by three are equal to the values of the corresponding index of l, but sorted.

    Test suite:
    >>> sorted(list_one)
    [1, 2, 3]
    >>> sorted(list_two)
    [2, 6, 3, 4, 8, 9, 5]
    """

    l = [1, 2, 3]
    l.sort_third()  # [1, 2, 3]
    l = [5, 6, 3, 4, 8, 9, 2]
    l.sort_third()  # [2, 6, 3, 4, 8, 9, 5]
    ```

This code defines a function named sort_third that sorts the elements of a list in a specific manner. It takes two list l as input and returns a new list l'. Then, it calls the function with two lists, list_one and list_two, and compares the resulting lists. The expected output for both tests is [1, 2, 3] for list_one and [2, 6, 3, 4, 8, 9, 5] for list_two.