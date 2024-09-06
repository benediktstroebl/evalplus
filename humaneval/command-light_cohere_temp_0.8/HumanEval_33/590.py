```python
def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indic that are not divisible by three, while its values at the indic that are divisible by three are equal to the values of the corresponding indic of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    >>> sort_third([10, 2, 15, 5, 6, 9, 8, 1])
    [1, 2, 5, 6, 8, 9, 10]
    """
    l=list(l)
    l=[x for x in l if x%3==0]
    l.sort()
    REMARKS:
    1. This function is **sorts out a list l' such that the values at the indices that are not divisible by three are the same as the values of the corresponding indices of l, but sorted**.
    2. This function does ** accept a value of type 'list' as l**.

# Example of testing the function
```python
def test_sort_third():
    l = [1, 2, 3]
    l2 = [5, 6, 3, 4, 8, 9, 2]
    print(sort_third(l))
    print(sort_third(l2))
    assert(l == l2)

test_sort_third()
```