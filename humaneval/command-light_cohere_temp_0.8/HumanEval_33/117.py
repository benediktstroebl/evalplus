```python
def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indic that are not divisible by three, while its values at the indic that are divisible by three are equal to the values of the corresponding indic of l, but sorted.

    Returns a test a list of numbers that are not divisible by three.

    # PEPED list
   
    n = len(l)
    l = [num for num in l if num % 3 != 0]
    l.extend(l)
    [num for num in l if num % 3 == 0])
    l = sorted(l)
    return l
```