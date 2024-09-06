```python
def sort_third(l: list):
    """This function takes a list l and returns a list l' such that l' is identical to l in the index that are not divisible by three, while its values at the index that are divisible by three are equal to the values of the corresponding index of l, but sorted.

    Returns list with built- test suite."""
    import numpy as np
    l = np.array(l)
    sort_third_new(l)
    return l
```
The script defines a function called sort_third that takes a list l as input and returns a new list l'. The function works by first creating a new list l_new that is identical to l in the index that are not divisible by three. Then, it sorts the array(l) and creates a new list l_new that is identical to l in the index that are divisible by three. The function then returns l_new.