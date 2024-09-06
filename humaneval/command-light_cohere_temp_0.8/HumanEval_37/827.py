```python
def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd index, while its values at the even index are equal to the values of the even index of l, but sorted.
    return: [1, 2, 3]
    """
    l.append(0)
    l.reverse()
   
    odd: list([i for i in range(len(l)) if l[i] % 2 == 1]))
    l = l[::-1]
    return l
```