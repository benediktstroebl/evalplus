```python
def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indic that are not divisible by three, while its values at the indic that are divisible by three are equal to the values of the corresponding indic of l, but sorted.
    """
Solve this problem for a list of numbers, where the numbers are greater than 0."""
    l = [1, 2, 3]
    for i in range(len(l)):
        if l[i] % 3 != 0:
            l[i] = l[i] + 1
    return l
```