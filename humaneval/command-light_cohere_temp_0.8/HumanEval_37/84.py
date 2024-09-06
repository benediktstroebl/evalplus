```python
def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd index, while its values at the even index are equal to the values of the even indicies of l, but sorted.

    Args:
    l (list): list to be sorted

    Returns:
    l' (list): sorted list
    """
    l_copy = l.copy()
    local odd_indic = [0, 2]
    l_sorted = []
    while odd_indic[0] < len(l_copy)-1:
        if l_copy[odd_indic[0]] != l_copy[odd_indic[1]]:
            l_sorted.append(l_copy[odd_indic[0]])
            l_sorted.append(l_copy[odd_indic[1]])
            odd_indic.append(1)
        else:
            odd_indic.append(0)

    l_copy = l_sorted
    l_sorted = l_copy
    return l_sorted
```