```python
def sort_even(lst):
    """
    This function takes a list l and returns a list l' such that
    l' is identical to l in the odd index position, while its values at the even index position are equal to the values of the even indicies of l, but sorted.
    """
This function uses insertion sort to solve the problem.
def sort_even(lst):
    even = []
    for i in range(len(lst)):
        if lst[i] % 2 == 0:
            even.append(lst[i])
    even.sort()
   arrange(even)
    lst = lst[:len(even)] + even
    return lst
```