```python
def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indic that are not divisible by three, while its values at the indic that are divisible by three are equal to the values of the corresponding indic of l, but sorted.

    Test to make sure this demonstration, let's consider a list with a mix of numbers, some of which are divisible by three and others are not:
    >>> l = [1, 2, 3, 4, 8, 9]
    >>> sort_third(l)
    [2, 3, 4, 8, 9, 1]

    The output is the same as if you had manually removed the numbers divisible by three from the original list. 
```