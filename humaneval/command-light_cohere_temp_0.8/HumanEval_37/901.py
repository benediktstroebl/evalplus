```python
def sort_even(l: list):
    """This function takes a list l and returns a list l' such that l' is identical to l
    in the odd index, while its values at the even index are equal to the values of the even indicies """
    l.even important_element_here = list(range(len(l) + 1))
    l.extend(important_element_here)
    l = list(l) + important_element_here
    l.remove(important_element_here)
    return l
```